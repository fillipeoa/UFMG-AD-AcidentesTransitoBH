import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# geometrias = [Point(float(x), float(y)) for x, y in zip(acidentes['COORDENADA_X'], acidentes['COORDENADA_Y'])]
# gdf_acidentes = gpd.GeoDataFrame(acidentes, geometry=geometrias)

FILEPATH_ACIDENTES = './data/acidentes/si-bol-20'
FILEPATH_VEICULOS = './data/veiculos/si-veic-20'
DATAINICIAL = 12
DATAFINAL = 22

import pandas as pd

def juntarAcidentesTotais():
    acidentesTotais = pd.DataFrame()

    # passar por todas as datas:
    for i in range(DATAINICIAL, DATAFINAL+1):
        acidentes = pd.read_csv(f'{FILEPATH_ACIDENTES}{i}.csv', delimiter=';', encoding='ISO-8859-1')
        
        # Strip whitespace and convert column names to uppercase
        acidentes.columns = acidentes.columns.str.strip().str.upper()

        acidentesTotais = pd.concat([acidentesTotais, acidentes])

    return acidentesTotais


def juntarVeiculosTotais():

    veiculosTotais = pd.DataFrame()

    # passar por todas as datas:
    for i in range(DATAINICIAL, DATAFINAL+1):
        veiculos = pd.read_csv(f'{FILEPATH_VEICULOS}{i}.csv', delimiter=';', encoding='ISO-8859-1')

        # Strip whitespace and convert column names to uppercase
        veiculos.columns = veiculos.columns.str.strip().str.upper()

        veiculosTotais = pd.concat([veiculosTotais, veiculos])

    return veiculosTotais


def gerarArquivosTotais():
    # Carrega os dados dos semáforos e dos acidentes
    acidentesTotais = juntarAcidentesTotais()
    # Colocar os dados em um arquivo csv
    acidentesTotais.to_csv('./data/acidentesTotais.csv', index=False)


    # Carrega os dados dos semáforos e dos acidentes
    veiculosTotais = juntarVeiculosTotais()
    # Colocar os dados em um arquivo csv
    veiculosTotais.to_csv('./data/veiculosTotais.csv', index=False)

    print(acidentesTotais.head())
    print(veiculosTotais.head())


def unirVeiculosAcidentes():
    # Carregar os dados dos acidentes e dos veículos
    acidentesTotais = pd.read_csv('./data/acidentesTotais.csv', delimiter=',', encoding='ISO-8859-1')
    acidentesTotais.columns = acidentesTotais.columns.str.strip()

    veiculosTotais = pd.read_csv('./data/veiculosTotais.csv', delimiter=',', encoding='ISO-8859-1')
    veiculosTotais.columns = veiculosTotais.columns.str.strip()

    # Verificar as colunas dos DataFrames
    print("Colunas em acidentesTotais:", acidentesTotais.columns)
    print("Colunas em veiculosTotais:", veiculosTotais.columns)

    # Certificar que a coluna 'NUMERO_BOLETIM' está presente em ambos os DataFrames
    if 'NUMERO_BOLETIM' not in acidentesTotais.columns:
        print("Coluna 'NUMERO_BOLETIM' não encontrada em acidentesTotais")
    if 'NUMERO_BOLETIM' not in veiculosTotais.columns:
        print("Coluna 'NUMERO_BOLETIM' não encontrada em veiculosTotais")

    # Para cada veículo, adicionar a informação do acidente e colocar as informações do acidente nas colunas seguintes, usando o 'NUMERO_BOLETIM' como chave
    acidentes_com_veiculos = pd.merge(acidentesTotais, veiculosTotais, on='NUMERO_BOLETIM', how='left')
    print("Colunas em acidentes_com_veiculos:", acidentes_com_veiculos.columns)
    # Salvar a nova tabela em um arquivo CSV
    acidentes_com_veiculos.to_csv('./data/acidentes.csv', index=False, sep=',', encoding='ISO-8859-1')

    print("Os dados foram unidos e salvos em 'acidentes.csv'.")

def getAcidentes():
    return pd.read_csv('./data/acidentes.csv', delimiter=',', encoding='ISO-8859-1', low_memory=False)


def getAcidentes():
    return pd.read_csv('./data/acidentes.csv', delimiter=',', encoding='ISO-8859-1', low_memory=False)

def getAcidentesPorRegiaoTotal():
    # Carregar os dados
    dataSetAcidentes = getAcidentes()

    # Filtrar acidentes com regiões válidas (não nulas e não vazias)
    dataSetAcidentes = dataSetAcidentes[dataSetAcidentes['DESC_REGIONAL'].notna() & (dataSetAcidentes['DESC_REGIONAL'].str.strip() != '')]

    # Extrair a data e a região
    dataSetAcidentes['DATA_BOLETIM'] = pd.to_datetime(dataSetAcidentes['DATA HORA_BOLETIM'], format='%d/%m/%Y %H:%M', errors='coerce')
    dataSetAcidentes['ANO'] = dataSetAcidentes['DATA_BOLETIM'].dt.year
    dataSetAcidentes = dataSetAcidentes[(dataSetAcidentes['ANO'] >= 2012) & (dataSetAcidentes['ANO'] <= 2022)]

    # Gráfico de barras: Regiões com mais acidentes
    acidentes_por_regiao = dataSetAcidentes['DESC_REGIONAL'].value_counts()

    plt.figure(figsize=(12, 8))
    acidentes_por_regiao.plot(kind='bar')
    plt.xlabel('Região')
    plt.ylabel('Quantidade de Acidentes')
    plt.title('Quantidade de Acidentes por Região')
    plt.show()


def getAcidentesPorRegiaoAno():
    # Carregar os dados
    dataSetAcidentes = getAcidentes()

    # Filtrar acidentes com regiões válidas (não nulas e não vazias)
    dataSetAcidentes = dataSetAcidentes[dataSetAcidentes['DESC_REGIONAL'].notna() & (dataSetAcidentes['DESC_REGIONAL'].str.strip() != '')]

    # Extrair a data e a região
    dataSetAcidentes['DATA_BOLETIM'] = pd.to_datetime(dataSetAcidentes['DATA HORA_BOLETIM'], format='%d/%m/%Y %H:%M', errors='coerce')
    dataSetAcidentes['ANO'] = dataSetAcidentes['DATA_BOLETIM'].dt.year
    dataSetAcidentes = dataSetAcidentes[(dataSetAcidentes['ANO'] >= 2012) & (dataSetAcidentes['ANO'] <= 2022)]

    # Gráfico de linhas: Quantidade de acidentes por ano para cada região
    acidentes_por_ano_regiao = dataSetAcidentes.groupby(['ANO', 'DESC_REGIONAL']).size().unstack(fill_value=0)

    plt.figure(figsize=(14, 10))
    for regiao in acidentes_por_ano_regiao.columns:
        plt.plot(acidentes_por_ano_regiao.index, acidentes_por_ano_regiao[regiao], marker='o', label=regiao)

    plt.xlabel('Ano')
    plt.ylabel('Quantidade de Acidentes')
    plt.title('Quantidade de Acidentes por Ano e Região (2012-2022)')
    plt.legend(title='Região', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.show()


# getAcidentesPorRegiaoAno();
veiculos = juntarVeiculosTotais();

#remover espaços em branco e converter para maiúsculas
veiculos['DESCRICAO_ESPECIE'] = veiculos['DESCRICAO_ESPECIE'].str.strip().str.upper()
#remover linahs com "NAO INFORMADO"
veiculos = veiculos[veiculos['DESCRICAO_ESPECIE'] != 'NAO INFORMADO']

#printar todos os tipos que existem:
print(veiculos['DESCRICAO_ESPECIE'].unique())

#Limpar dados com menos de 100 registros
veiculos = veiculos[veiculos['DESCRICAO_ESPECIE'].map(veiculos['DESCRICAO_ESPECIE'].value_counts()) > 500]

# # gerar um GRAFICO de barras COM os veículos mais comuns (DESCRICAO_ESPECIE) ignorando campos vazios e 
# veiculos['DESCRICAO_ESPECIE'].value_counts().dropna().plot(kind='bar')
# plt.xlabel('Categoria de Veículo')
# plt.ylabel('Quantidade')
# plt.title('Veículos Mais Comuns')
# plt.show()

# gerar um GRAFICO de PIZZA COM os veículos mais comuns (DESCRICAO_ESPECIE) ignorando campos vazios
veiculos['DESCRICAO_ESPECIE'].value_counts().dropna().plot(kind='pie')
plt.title('Veículos Mais Comuns')
plt.show()
