### README

# Análise de Acidentes de Trânsito com Monte Carlo Tree Search (MCTS)

Este repositório contém o código e os dados utilizados para a análise de acidentes de trânsito com vítimas em Belo Horizonte, utilizando o algoritmo Monte Carlo Tree Search (MCTS). O trabalho é baseado na implementação disponível no repositório [MCTS4DM](https://github.com/guillaume-bosc/MCTS4DM), que fornece uma ferramenta avançada para a descoberta de subgrupos e mineração de padrões.

## Estrutura do Repositório

- **`analise_exploratoria/`**: Contém as bases de dados originais e scripts utilizados para geração
das analises preliminares


- **`descoberta_subgrupos_mcts/`**: Contém as bases de dados, scripts utilizados e resultados da aplicação do MCTS
  - **`datasets/`**: Contém os arquivos de dados utilizados na análise. Os dados foram processados e adaptados para o formato necessário para a execução do MCTS em cada caso.
    - **`properties.csv`**: Este arquivo contém a base completa de dados, com atributos relevantes para a análise, como datas dos acidentes, tipos de veículos, e outras informações contextuais.
    - **`qualities.csv`**: Contém uma coluna com o atributo específico da medida de qualidade analisada. Este arquivo é utilizado para definir as metas da análise com o MCTS.

  - **`src/`**: Contém scripts em Python utilizados para a preparação dos dados
    - **`geracao_entradas_mcts.py`**: Script responsável pela limpeza dos dados, tratamento de valores inválidos, criação de novas colunas (como dia da semana e período do dia), e preparação final para uso no MCTS.
    
  - **`resultados/`**: Contém resultados gerados na descoberta de subgrupos
 
## Como Executar

1. **Preparação do Ambiente**: Configure o ambiente para a execução do MCTS, conforme descrito no [repositório MCTS4DM](https://github.com/guillaume-bosc/MCTS4DM). Certifique-se de ter o Java instalado e configurado corretamente.

2. **Execução do MCTS**: Utilize os arquivos de dados `properties.csv` e `qualities.csv` presentes em cada pasta dentro de `descoberta_subgrupos_mcts/datasets/` como entrada para o algoritmo MCTS. Siga as instruções do repositório base paran cofigurar os parâmetros, rodar o MCTS e explorar os padrões e subgrupos descobertos.

3. **Análise dos Resultados**: Após a execução do MCTS, analise os padrões identificados para obter insights sobre os acidentes de trânsito em Belo Horizonte. Os resultados podem ser usados para formular políticas de segurança viária e intervenções específicas.
