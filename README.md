# Sistema Especialista de Diagnóstico de TI

Este é um sistema especialista simples e eficaz implementado em Python para diagnóstico preliminar de problemas de computador. O sistema analisa descrições textuais de problemas e fornece diagnósticos possíveis com soluções práticas.

## Como funciona

O sistema solicita uma descrição textual do problema do usuário, analisa o texto procurando por palavras-chave relacionadas a sintomas comuns de TI, e fornece até 3 diagnósticos mais prováveis ordenados por nível de confiança.

Os dados usados no diagnóstico ficam no arquivo `base_conhecimento.json` (no mesmo diretório do `main.py`). Você pode editar esse arquivo para adicionar/alterar problemas, palavras‑chave, soluções e severidades sem precisar mexer no código.

## Recursos

- **Análise Textual Inteligente**: Sistema analisa descrições em linguagem natural
- **Correspondência Robusta**: Normalização (acentos/caso), frases inteiras com bordas de palavra e suporte simples a flexões (ex.: "conectar" → "conectando")
- **Base de Conhecimento em JSON**: Facilmente editável em `base_conhecimento.json`
- **Sistema de Palavras-Chave**: Identifica sintomas automaticamente no texto
- **Pontuação de Confiança**: Cada diagnóstico inclui porcentagem de confiança
- **Soluções Práticas**: Sugestões de reparo para cada problema identificado
- **Níveis de Severidade**: Problemas categorizados como Baixo, Médio ou Alto
- **Interface Interativa**: Permite múltiplas consultas na mesma sessão
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

<!-- Modo Demonstração removido: a aplicação agora exige uso interativo em terminal -->

## Problemas Diagnosticados

O sistema identifica os seguintes tipos de problemas:

Alguns exemplos (não exaustivo):

1. **Problema de Performance** — Lento, travando, demora para abrir
2. **Infecção por Malware** — Pop‑ups, anúncios suspeitos
3. **Problema de Hardware** — Travamentos, tela azul
4. **Conectividade/Internet** — Internet/rede, DNS, VPN, Wi‑Fi intermitente, proxy
5. **Armazenamento** — Disco cheio, partição/SO de arquivos corrompidos
6. **Sobreaquecimento** — CPU/GPU quentes, pasta térmica, poeira, ventoinha com falha, throttling
7. **Periféricos** — Mouse, teclado, impressora, USB
8. **Sistema Operacional** — Inicialização/boot, atualizações do sistema
9. **Vídeo/Áudio** — Tela preta, resolução, som/microfone
10. **Software/Aplicativos** — Não abre apps, não responde, fecha sozinho
11. **E‑mail/Navegador** — Envio/recebimento, cache, extensões, SSL
12. **Sincronização e Backup** — OneDrive/Drive/Dropbox, falha de backup

## Propósito Educacional

Este sistema demonstra conceitos fundamentais de IA:
- **Sistemas especialistas baseados em regras**
- **Processamento de linguagem natural básico** (análise de palavras-chave)
- **Algoritmos de correspondência e pontuação**
- **Interface conversacional simples**
- **Lógica de diagnóstico automatizado**
