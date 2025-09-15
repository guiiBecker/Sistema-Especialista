#!/usr/bin/env python3
"""
Sistema Especialista de Diagnóstico de TI
Sistema que analisa descrições de problemas de computador e fornece diagnósticos possíveis.
"""

BASE_CONHECIMENTO = {
    "problema_lentidao": {
        "palavras_chave": ["lento", "devagar", "performance", "lentidão", "trava", "congela",
                          "demora", "carrega", "resposta", "atraso", "desempenho", "velocidade"],
        "diagnostico": "Problema de Performance",
        "solucao": "Verificar uso de CPU/memória, fechar programas desnecessários, verificar disco",
        "severidade": "Médio"
    },
    "problema_malware": {
        "palavras_chave": ["vírus", "malware", "popup", "anúncio", "suspeito", "estranho"],
        "diagnostico": "Possível Infecção por Malware",
        "solucao": "Executar antivírus completo, verificar downloads recentes, limpar cache",
        "severidade": "Alto"
    },
    "problema_hardware": {
        "palavras_chave": ["trava", "reinicia", "tela azul", "erro", "crash", "quebrado"],
        "diagnostico": "Problema de Hardware",
        "solucao": "Verificar RAM, disco rígido, temperatura, conexões físicas",
        "severidade": "Alto"
    },
    "problema_rede": {
        "palavras_chave": ["internet", "rede", "conexão", "wifi", "conectar", "online",
                          "navegador", "site", "carregar", "página", "rede lenta"],
        "diagnostico": "Problema de Conectividade",
        "solucao": "Reiniciar modem, verificar cabos, testar com outro dispositivo",
        "severidade": "Baixo"
    },
    "problema_armazenamento": {
        "palavras_chave": ["espaço", "disco", "cheio", "armazenamento", "memória", "HD"],
        "diagnostico": "Problema de Armazenamento",
        "solucao": "Liberar espaço, excluir arquivos temporários, verificar disco",
        "severidade": "Médio"
    },
    "problema_sobreaquecimento": {
        "palavras_chave": ["quente", "ventoinha", "temperatura", "aquecer", "superaquecer"],
        "diagnostico": "Problema de Sobreaquecimento",
        "solucao": "Limpar ventoinhas, verificar ventilação, usar base elevada",
        "severidade": "Médio"
    },
    "problema_perifericos": {
        "palavras_chave": ["mouse", "teclado", "impressora", "usb", "periférico", "não funciona"],
        "diagnostico": "Problema com Periféricos",
        "solucao": "Verificar conexões, atualizar drivers, testar em outra porta",
        "severidade": "Baixo"
    },
    "problema_sistema": {
        "palavras_chave": ["iniciar", "boot", "ligar", "sistema", "windows", "instalar"],
        "diagnostico": "Problema do Sistema Operacional",
        "solucao": "Executar inicialização limpa, verificar disco, restaurar sistema",
        "severidade": "Alto"
    }
}

def analisar_descricao(descricao):
    """
    Analisa a descrição do problema e encontra possíveis diagnósticos
    Retorna lista de diagnósticos ordenados por relevância
    """
    descricao_minuscula = descricao.lower()
    resultados = []

    for problema, dados in BASE_CONHECIMENTO.items():
        pontuacao = 0
        palavras_encontradas = []

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
        "Não consigo conectar à internet mas outros dispositivos funcionam"
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
