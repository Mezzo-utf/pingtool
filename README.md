# Pyng_tool

Este projeto implementa uma ferramenta simples de *ping* que permite testar a conectividade de rede com um host (por meio de um endereço IP ou URL) e medir o tempo de resposta. A ferramenta executa um ping contínuo no host até que o usuário a interrompa manualmente.

## Funcionalidades

- Testa a conectividade com um host usando o protocolo ICMP.
- Exibe o tempo de resposta para cada ping, em milissegundos.
- Permite monitoramento contínuo da rede com intervalos de 1 segundo entre cada ping.
- Interrompe a execução com a combinação de teclas `Ctrl+C`.

## Requisitos

- Python 3.x
- Biblioteca `ping3` (pode ser instalada via `pip`)

## Instalação

1. Clone este repositório para o seu computador:
   ```bash
   git clone https://github.com/seu-usuario/ferramenta-de-ping.git
2. Instale a dependência do ping
   ```bash
   pip install ping3
---
## Como usar

1. Execute o script:
   ```bash
   python pyng_tool.py
2. Digite o endereço IP ou URL do host que deseja testar:
   ```
   example.com
3. O script irá mostrar o tempo de resposta de cada ping, como no exemplo:
  ```bash
   Tempo de resposta para example.com: 34.12 ms
```
## Possíveis Melhorias

Este projeto tem várias possibilidades de aprimoramento, e pretendo continuar aprimorando ao longo do próximo ano. Algumas ideias incluem:

- **Histórico de Pings**: Armazenar os tempos de resposta em um arquivo de log ou banco de dados, permitindo análise posterior. Também seria interessante exibir a média, o valor mínimo e o valor máximo dos tempos de resposta após uma execução de pings.

- **Gráficos de Desempenho**: Gerar gráficos em tempo real que mostrem os tempos de resposta de cada ping, usando bibliotecas como `matplotlib` ou `plotly`, permitindo uma visualização mais interativa e útil para o usuário.

- **Interface Gráfica (GUI)**: Construir uma interface gráfica usando bibliotecas como `tkinter`, `PyQt` ou `Kivy`, permitindo que o usuário interaja com o programa de forma mais amigável. A GUI poderia incluir a inserção do endereço do host, exibição em tempo real dos resultados e gráficos de desempenho.

- **Ping em Múltiplos Hosts**: Permitir a execução do ping em múltiplos hosts simultaneamente, exibindo os resultados para cada um. Isso pode ser útil em ambientes de rede onde é necessário verificar a conectividade com diversos dispositivos ao mesmo tempo.

