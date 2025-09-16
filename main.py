#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from typing import Any, Dict, List


def _caminho_base_json() -> str:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "base_conhecimento.json")


def carregar_base_conhecimento(caminho: str | None = None) -> Dict[str, Dict[str, Any]]:
    """Carrega a base de conhecimento a partir do JSON."""
    caminho = caminho or _caminho_base_json()
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                raise ValueError(
                    "JSON da base de conhecimento deve ser um objeto no topo"
                )
            return data
    except FileNotFoundError:
        raise SystemExit(f"Arquivo de base de conhecimento não encontrado: {caminho}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"Erro ao ler JSON da base de conhecimento: {e}")


BASE_CONHECIMENTO = carregar_base_conhecimento()


def analisar_descricao(descricao: str) -> List[Dict[str, Any]]:
    descricao_minuscula = descricao.lower()
    resultados: List[Dict[str, Any]] = []

    for problema, dados in BASE_CONHECIMENTO.items():
        pontuacao = 0
        palavras_encontradas: List[str] = []

        for palavra in dados["palavras_chave"]:
            if palavra in descricao_minuscula:
                pontuacao += 1
                palavras_encontradas.append(palavra)

        if pontuacao > 0:
            confianca = min(pontuacao / len(dados["palavras_chave"]), 1.0)
            resultados.append(
                {
                    "diagnostico": dados["diagnostico"],
                    "solucao": dados["solucao"],
                    "severidade": dados["severidade"],
                    "confianca": confianca,
                    "palavras": palavras_encontradas,
                }
            )

    # Ordenar por confiança
    resultados.sort(key=lambda x: x["confianca"], reverse=True)

    return resultados[:3]  # Retornar top 3


def obter_descricao_usuario():
    """Solicita a descrição do problema ao usuário."""
    print("=== SISTEMA ESPECIALISTA DE DIAGNÓSTICO DE TI ===")
    print("Descreva o problema que você está enfrentando com seu computador.")
    print("Seja o mais detalhado possível - mencione sintomas, quando começou, etc.")
    print("Digite 'sair' para encerrar.\n")

    while True:
        try:
            descricao = input("Descrição do problema: ").strip()

            if descricao.lower() == "sair":
                return None

            if len(descricao) < 5:
                print(
                    "Por favor, forneça uma descrição mais detalhada (mínimo 5 caracteres)."
                )
                continue

            return descricao

        except KeyboardInterrupt:
            print("\nPrograma interrompido pelo usuário.")
            return None
        except EOFError:
            return None


def mostrar_diagnosticos(resultados, descricao):
    print(f'\nAnalisando: "{descricao}"\n')

    if not resultados:
        print("Não foi possível identificar problemas específicos na sua descrição.")
        print("Tente fornecer mais detalhes sobre os sintomas.")
        return

    print("=" * 60)
    print("DIAGNÓSTICOS POSSÍVEIS:")
    print("=" * 60)

    for i, resultado in enumerate(resultados, 1):
        print(f"\n{i}. {resultado['diagnostico']}")
        print(f"   Confiança: {resultado['confianca']:.1%}")
        print(f"   Severidade: {resultado['severidade']}")
        print(f"   Solução: {resultado['solucao']}")
        if resultado["palavras"]:
            print(f"   Palavras identificadas: {', '.join(resultado['palavras'])}")

    print("\n" + "=" * 60)


def main():
    try:
        import sys

        if not sys.stdin.isatty():
            print(
                "Entrada interativa não disponível. Execute em um terminal para usar o sistema."
            )
            return
    except Exception:
        pass

    while True:
        descricao = obter_descricao_usuario()

        if descricao is None:
            print("Encerrado")
            break

        # Se não houver descrição (ex.: EOF), encerra
        resultados = analisar_descricao(descricao)

        mostrar_diagnosticos(resultados, descricao)

        try:
            continuar = (
                input("\nDeseja diagnosticar outro problema? (s/n): ").strip().lower()
            )
            if continuar not in ["s", "sim", "y", "yes"]:
                print("Encerrado")
                break
        except (KeyboardInterrupt, EOFError):
            print("\nPrograma encerrado.")
            break

        print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main()
