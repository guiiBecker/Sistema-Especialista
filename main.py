#!/usr/bin/env python3
"""
Sistema Especialista de Diagnóstico de TI
Sistema que analisa descrições de problemas de computador e fornece diagnósticos possíveis.
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List


def _caminho_base_json() -> str:
    """Resolve o caminho do arquivo base_conhecimento.json relativo a este script."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "base_conhecimento.json")


def carregar_base_conhecimento(caminho: str | None = None) -> Dict[str, Dict[str, Any]]:
    """Carrega a base de conhecimento a partir de um arquivo JSON.

    Estrutura esperada:
    {
      "chave": {
        "palavras_chave": ["..."],
        "diagnostico": "...",
        "solucao": "...",
        "severidade": "Alto|Médio|Baixo"
      },
      ...
    }
    """
    caminho = caminho or _caminho_base_json()
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                raise ValueError("JSON da base de conhecimento deve ser um objeto no topo")
            return data  # type: ignore[return-value]
    except FileNotFoundError:
        raise SystemExit(f"Arquivo de base de conhecimento não encontrado: {caminho}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"Erro ao ler JSON da base de conhecimento: {e}")

BASE_CONHECIMENTO = carregar_base_conhecimento()


def analisar_descricao(descricao: str) -> List[Dict[str, Any]]:
    """
    Analisa a descrição do problema e encontra possíveis diagnósticos
    Retorna lista de diagnósticos ordenados por relevância
    """
    descricao_minuscula = descricao.lower()
    resultados: List[Dict[str, Any]] = []

    for problema, dados in BASE_CONHECIMENTO.items():
        pontuacao = 0
        palavras_encontradas: List[str] = []

        # Verificar cada palavra-chave
        for palavra in dados["palavras_chave"]:
            if palavra in descricao_minuscula:
                pontuacao += 1
                palavras_encontradas.append(palavra)

        if pontuacao > 0:
            # Calcular confiança baseada no número de palavras encontradas
            confianca = min(pontuacao / len(dados["palavras_chave"]), 1.0)
            resultados.append({
                "diagnostico": dados["diagnostico"],
                "solucao": dados["solucao"],
                "severidade": dados["severidade"],
                "confianca": confianca,
                "palavras": palavras_encontradas
            })

    # Ordenar por confiança
    resultados.sort(key=lambda x: x["confianca"], reverse=True)

    return resultados[:3]  # Retornar top 3

def obter_descricao_usuario():
    """Obtém a descrição do problema do usuário"""
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
            return "MODO_DEMONSTRACAO"

def mostrar_diagnosticos(resultados, descricao):
    """Mostra os diagnósticos encontrados"""
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
    print("NOTA: Este é um diagnóstico preliminar baseado em IA.")
    print("Consulte um técnico especializado para reparo adequado.")

def modo_demonstracao():
    """Mostra exemplos de funcionamento do sistema"""
    print("=== MODO DEMONSTRAÇÃO ===")
    print("Como não há entrada interativa disponível, aqui estão alguns exemplos:\n")

    exemplos = [
        "Meu computador está muito lento e demora para abrir os programas",
        "Aparecem muitos pop-ups e anúncios suspeitos na tela",
        "O computador travou e mostrou tela azul de erro",
        "Não consigo conectar à internet mas outros dispositivos funcionam",
        "O disco rígido está quase cheio e os arquivos não salvam",
        "O notebook fica muito quente e a ventoinha não para",
        "O mouse e o teclado não estão funcionando",
        "O Windows não inicia corretamente e reinicia sozinho",
        "O som parou de funcionar após atualizar a placa de vídeo",
        "A bateria do notebook descarrega muito rápido e não carrega completamente",
        "Não consigo enviar nem receber mensagens no Outlook",
        "O microfone não está captando minha voz",
        "O monitor está com a tela preta, mas o computador está ligado",
        "Não consigo acessar a impressora compartilhada na rede",
        "O aplicativo trava e fecha sozinho toda vez que abro",
        "Minha conexão de internet está muito lenta, downloads demorando horas"
    ]

    for i, exemplo in enumerate(exemplos, 1):
        print(f"EXEMPLO {i}:")
        resultados = analisar_descricao(exemplo)
        mostrar_diagnosticos(resultados, exemplo)
        print("-" * 60)

    print("\nPara usar o sistema completo:")
    print("python3 main.py")
    print("E forneça suas próprias descrições!")

def main():
    """Função principal do programa"""

    try:
        import sys
        if not sys.stdin.isatty():
            modo_demonstracao()
            return
    except:
        modo_demonstracao()
        return

    while True:
        descricao = obter_descricao_usuario()

        if descricao is None:
            print("Obrigado por usar o Sistema Especialista de Diagnóstico de TI!")
            break

        if descricao == "MODO_DEMONSTRACAO":
            modo_demonstracao()
            break

        resultados = analisar_descricao(descricao)

    
        mostrar_diagnosticos(resultados, descricao)

        try:
            continuar = input("\nDeseja diagnosticar outro problema? (s/n): ").strip().lower()
            if continuar not in ['s', 'sim', 'y', 'yes']:
                print("Obrigado por usar o Sistema Especialista de Diagnóstico de TI!")
                break
        except (KeyboardInterrupt, EOFError):
            print("\nPrograma encerrado.")
            break

        print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()
