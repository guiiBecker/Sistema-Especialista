#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from typing import Any, Dict, List
import re
import unicodedata


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
                raise ValueError("JSON da base de conhecimento deve ser um objeto no topo")
            return data
    except FileNotFoundError:
        raise SystemExit(f"Arquivo de base de conhecimento não encontrado: {caminho}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"Erro ao ler JSON da base de conhecimento: {e}")

BASE_CONHECIMENTO = carregar_base_conhecimento()


def analisar_descricao(descricao: str) -> List[Dict[str, Any]]:
    """Analisa a descrição e retorna diagnósticos ordenados."""
    def _normalizar_texto(s: str) -> str:
        s = s.lower()
        s = unicodedata.normalize("NFD", s)
        s = "".join(c for c in s if unicodedata.category(c) != "Mn")
        s = re.sub(r"\s+", " ", s).strip()
        return s

    def _tem_negacao_perto(texto_norm: str, start_idx: int, janela_chars: int = 25) -> bool:
        ini = max(0, start_idx - janela_chars)
        contexto = texto_norm[ini:start_idx]
        return bool(re.search(r"\bnao\b|\bn\u00e3o\b", contexto))

    descricao_minuscula = _normalizar_texto(descricao)
    resultados: List[Dict[str, Any]] = []

    for problema, dados in BASE_CONHECIMENTO.items():
        pontuacao = 0.0
        palavras_encontradas: List[str] = []

        for palavra in dados["palavras_chave"]:
            kw_norm = _normalizar_texto(palavra)
            matched = False
            peso = 1.0

            if " " in kw_norm:
                padrao = r"\b" + re.escape(kw_norm) + r"\b"
                m = re.search(padrao, descricao_minuscula)
                if m:
                    matched = True
                    peso = 1.5
                    if _tem_negacao_perto(descricao_minuscula, m.start()):
                        peso += 0.3
            else:
                padrao_exato = r"\b" + re.escape(kw_norm) + r"\b"
                m = re.search(padrao_exato, descricao_minuscula)
                if m:
                    matched = True
                    if _tem_negacao_perto(descricao_minuscula, m.start()):
                        peso += 0.3
                else:
                    if kw_norm.endswith(("ar", "er", "ir")) and len(kw_norm) >= 5:
                        raiz = kw_norm[:-2]
                        padrao_raiz = r"\b" + re.escape(raiz) + r"\w*\b"
                        m2 = re.search(padrao_raiz, descricao_minuscula)
                        if m2:
                            matched = True
                            if _tem_negacao_perto(descricao_minuscula, m2.start()):
                                peso += 0.3

            if matched:
                pontuacao += peso
                palavras_encontradas.append(palavra)

        if pontuacao > 0:
            max_peso = sum(1.5 if " " in _normalizar_texto(p) else 1.0 for p in dados["palavras_chave"])
            confianca = min(pontuacao / max_peso, 1.0)
            resultados.append({
                "diagnostico": dados["diagnostico"],
                "solucao": dados["solucao"],
                "severidade": dados["severidade"],
                "confianca": confianca,
                "palavras": palavras_encontradas
            })

    prioridade = {"Alto": 3, "Médio": 2, "Baixo": 1, "Medio": 2}
    resultados.sort(key=lambda x: (x["confianca"], prioridade.get(x["severidade"], 0)), reverse=True)

    return resultados[:3]

def obter_descricao_usuario():
    """Solicita a descrição do problema ao usuário."""
    print("=== SISTEMA ESPECIALISTA DE DIAGNÓSTICO DE TI ===")
    print("Descreva o problema que você está enfrentando com seu computador.")
    print("Seja o mais detalhado possível - mencione sintomas, quando começou, etc.")
    print("Digite 'sair' para encerrar.\n")

    while True:
        try:
            descricao = input("Descrição do problema: ").strip()

            if descricao.lower() == 'sair':
                return None

            if len(descricao) < 5:
                print("Por favor, forneça uma descrição mais detalhada (mínimo 5 caracteres).")
                continue

            return descricao

        except KeyboardInterrupt:
            print("\nPrograma interrompido pelo usuário.")
            return None
        except EOFError:
            return None

def mostrar_diagnosticos(resultados, descricao):
    """Exibe os diagnósticos formatados."""
    print(f"\nAnalisando: \"{descricao}\"\n")

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
        if resultado['palavras']:
            print(f"   Palavras identificadas: {', '.join(resultado['palavras'])}")

    print("\n" + "=" * 60)


def main():
    """Ponto de entrada do programa."""
    try:
        import sys
        if not sys.stdin.isatty():
            print("Entrada interativa não disponível. Execute em um terminal para usar o sistema.")
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
            continuar = input("\nDeseja diagnosticar outro problema? (s/n): ").strip().lower()
            if continuar not in ['s', 'sim', 'y', 'yes']:
                print("Encerrado")
                break
        except (KeyboardInterrupt, EOFError):
            print("\nPrograma encerrado.")
            break

        print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()
