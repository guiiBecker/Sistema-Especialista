# Sistema Especialista de Diagnóstico de TI

Este é um sistema especialista simples e eficaz implementado em Python para diagnóstico preliminar de problemas de computador. O sistema analisa descrições textuais de problemas e fornece diagnósticos possíveis com soluções práticas.

## Como funciona

O sistema solicita uma descrição textual do problema do usuário, analisa o texto procurando por palavras-chave relacionadas a sintomas comuns de TI, e fornece até 3 diagnósticos mais prováveis ordenados por nível de confiança.

Os dados usados no diagnóstico ficam no arquivo `base_conhecimento.json` (no mesmo diretório do `main.py`). Você pode editar esse arquivo para adicionar/alterar problemas, palavras‑chave, soluções e severidades sem precisar mexer no código.

## Recursos

- **Análise Textual Inteligente**: Sistema analisa descrições em linguagem natural
- **Base de Conhecimento Estruturada**: 8 tipos de problemas comuns de TI
- **Sistema de Palavras-Chave**: Identifica sintomas automaticamente no texto
- **Pontuação de Confiança**: Cada diagnóstico inclui porcentagem de confiança
- **Soluções Práticas**: Sugestões de reparo para cada problema identificado
- **Níveis de Severidade**: Problemas categorizados como Baixo, Médio ou Alto
- **Interface Interativa**: Permite múltiplas consultas na mesma sessão
- **Modo Demonstração**: Mostra exemplos quando executado sem entrada interativa
- **Implementação Simples**: Código puro em Python, fácil de entender

## Como executar

1. Certifique-se de ter o Python 3 instalado
2. Abra um terminal neste diretório
3. Execute: `python3 main.py`
4. Descreva o problema do seu computador em linguagem natural
5. O sistema analisará sua descrição e fornecerá diagnósticos

Se você editar o `base_conhecimento.json`, as mudanças são carregadas automaticamente na próxima execução.

### Como editar a base de conhecimento

1. Abra o arquivo `base_conhecimento.json` neste diretório.
2. Cada item possui a estrutura:
    ```json
    "chave_do_problema": {
       "palavras_chave": ["...", "..."],
       "diagnostico": "Descrição do diagnóstico",
       "solucao": "Sugestão de solução",
       "severidade": "Alto|Médio|Baixo"
    }
    ```
3. Salve o arquivo e rode `python3 main.py` novamente.

## Exemplo de Uso

```
=== SISTEMA ESPECIALISTA DE DIAGNÓSTICO DE TI ===
Descreva o problema que você está enfrentando com seu computador.
Seja o mais detalhado possível - mencione sintomas, quando começou, etc.
Digite 'sair' para encerrar.

Descrição do problema: Meu computador está muito lento e demora para abrir os programas

Analisando: "Meu computador está muito lento e demora para abrir os programas"

============================================================
DIAGNÓSTICOS POSSÍVEIS:
============================================================

1. Problema de Performance
   Confiança: 16.7%
   Severidade: Médio
   Solução: Verificar uso de CPU/memória, fechar programas desnecessários, verificar disco
   Palavras identificadas: lento, demora

============================================================
NOTA: Este é um diagnóstico preliminar baseado em IA.
Consulte um técnico especializado para reparo adequado.

Deseja diagnosticar outro problema? (s/n):
```

## Modo Demonstração

Quando executado em ambientes não-interativos (como pipes ou scripts), o sistema mostra exemplos de funcionamento:

```
=== MODO DEMONSTRAÇÃO ===
Como não há entrada interativa disponível, aqui estão alguns exemplos:

EXEMPLO 1: [diagnóstico para problema de lentidão]
EXEMPLO 2: [diagnóstico para problema de malware]
EXEMPLO 3: [diagnóstico para problema de hardware]
EXEMPLO 4: [diagnóstico para problema de rede]
```

## Problemas Diagnosticados

O sistema identifica os seguintes tipos de problemas:

1. **Problema de Performance** - Computador lento, travamentos, demora para abrir programas
2. **Infecção por Malware** - Pop-ups, anúncios suspeitos, comportamento estranho
3. **Problema de Hardware** - Travamentos, tela azul, reinicializações inesperadas
4. **Problema de Conectividade** - Internet lenta, problemas de rede, WiFi
5. **Problema de Armazenamento** - Disco cheio, falta de espaço
6. **Sobreaquecimento** - Computador quente, ventoinhas ruidosas
7. **Problemas com Periféricos** - Mouse, teclado, impressora não funcionam
8. **Problema do Sistema Operacional** - Dificuldade para iniciar, boot problems

## Propósito Educacional

Este sistema demonstra conceitos fundamentais de IA:
- **Sistemas especialistas baseados em regras**
- **Processamento de linguagem natural básico** (análise de palavras-chave)
- **Algoritmos de correspondência e pontuação**
- **Interface conversacional simples**
- **Lógica de diagnóstico automatizado**
