import pandas as pd

def gerar_csv_limpo():
    data = pd.read_csv('datasets/Acidentes/acidentes_veiculos.csv', low_memory=False)
    
    # LIMPAR NOMES DAS COLUNAS, REMOVER ACENTOS E CARACTERES ESPECIAIS E REMOVER ESPAÇOS EM BRANCO
    data.columns = data.columns.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    #Limpar os dados das linhas REMOVER ACENTOS E CARACTERES ESPECIAIS E REMOVER ESPAÇOS EM BRANCO
    data = data.apply(lambda x: x.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8') if x.dtype == "object" else x)
    #remover espaços em branco
    data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    data.to_csv('datasets/Acidentes/acidentes_veiculos_limpo.csv', index=False, sep='\t')

def gerar_entradas_acidentes_ocorridos():
    dados = pd.read_csv('datasets/Acidentes/acidentes_veiculos_limpo.csv', low_memory=False, sep='\t')

    colunas_selecionadas = [
    #'NUMERO_BOLETIM',
    'DATA HORA_BOLETIM',
    #'DATA_INCLUSAO',
    #'TIPO_ACIDENTE',
    'DESC_TIPO_ACIDENTE',
    #'COD_TEMPO',
    'DESC_TEMPO',
    #'COD_PAVIMENTO',
    'PAVIMENTO',
    #'COD_REGIONAL',
    'DESC_REGIONAL',
    #'ORIGEM_BOLETIM',
    'LOCAL_SINALIZADO',
    #'VELOCIDADE_PERMITIDA',
    #'COORDENADA_X',
    #'COORDENADA_Y',
    #'HORA_INFORMADA',
    #'INDICADOR_FATALIDADE',
    #'VALOR_UPS',
    #'DESCRICAO_UPS',
    #'DATA_ALTERACAO_SMSA',
    #'VALOR_UPS_ANTIGA',
    #'DESCRICAO_UPS_ANTIGA',
    #'DESCRICAO_UPS',
    #'DESCRICAO_UPS_ANTIGA',
    #'DATA_HORA_BOLETIM',
    #'SEQUENCIAL_VEICULO',
    #'CODIGO_CATEGORIA',
    'DESCRICAO_CATEGORIA',
    #'CODIGO_ESPECIE',
    'DESCRICAO_ESPECIE',
    #'CODIGO_SITUACAO',
    'DESCRICAO_SITUACAO',
    #'TIPO_SOCORRO',
    #'DESCRICAO_TIPO_SOCORRO',
    #'No_BOLETIM',
    #'SEQ_VEIC',
    #'COD_CATEG',
    #'COD_ESPECIE',
    #'COD_SITUACAO',
    #'DESC_SITUACAO',
    #'DESC_TIPO_SOCORRO',
    'HORARIO',
    'DIA_SEMANA'
    ]

    # Criar nova coluna HORARIO com base na hora informada (PICO 1/MANHÃ/TARDE/PICO 2/NOITE/MADRUGADA)
    dados['HORARIO'] = pd.to_datetime(dados['DATA HORA_BOLETIM'], format='%d/%m/%Y %H:%M').dt.hour
    dados['HORARIO'] = dados['HORARIO'].apply(lambda x: 'PICO 1' if 6 <= x < 9 else 'MANHÃ' if 9 <= x < 12 else 'TARDE' if 12 <= x < 16 else 'PICO 2' if 16 <= x < 19 else 'NOITE' if 19 <= x <= 23 else 'MADRUGADA')

    #Criar nova coluna DIA_SEMANA com base na DATA HORA_BOLETIM
    dados['DIA_SEMANA'] = pd.to_datetime(dados['DATA HORA_BOLETIM'], format='%d/%m/%Y %H:%M').dt.day_name()
    dados['DIA_SEMANA'] = dados['DIA_SEMANA'].replace(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], ['SEGUNDA-FEIRA', 'TERÇA-FEIRA', 'QUARTA-FEIRA', 'QUINTA-FEIRA', 'SEXTA-FEIRA', 'SÁBADO', 'DOMINGO'])

    # GERAR ARQUIVO PROPERTIES
    properties = dados[colunas_selecionadas]
    #Remova todas as linhas que tem alguma das colunas filtradas com valor vazio
    #properties = properties.dropna(subset=colunas_selecionadas)
    #Remova todas as linhas que tem alguma das colunas filtradas com valor NÃO INFORMADO
    #properties = properties[~properties.isin(['NÃO INFORMADO','NAO INFORMADO']).any(axis=1)]
    properties.to_csv('datasets/Acidentes/ocorridos/properties.csv', index=False, sep='\t')

    # GERAR ARQUIVO QUALITIES
    qualities = pd.DataFrame([1]*len(properties), columns=['OCORRIDO'])
    qualities.to_csv('datasets/Acidentes/ocorridos/qualities.csv', index=False, sep='\t')

def gerar_entradas_acidentes_ocorridos_centro_sul():
    dados = pd.read_csv('datasets/Acidentes/acidentes_veiculos_limpo.csv', low_memory=False, sep='\t')

    colunas_selecionadas = [
    #'NUMERO_BOLETIM',
    'DATA HORA_BOLETIM',
    #'NUMERO_BOLETIM',
    #'TIPO_ACIDENTE',
    'DESC_TIPO_ACIDENTE',
    #'COD_TEMPO',
    'DESC_TEMPO',
    #'COD_PAVIMENTO',
    'PAVIMENTO',
    #'COD_REGIONAL',
    #'DESC_REGIONAL',
    #'ORIGEM_BOLETIM',
    'LOCAL_SINALIZADO',
    #'VELOCIDADE_PERMITIDA',
    #'COORDENADA_X',
    #'COORDENADA_Y',
    #'HORA_INFORMADA',
    #'INDICADOR_FATALIDADE',
    #'VALOR_UPS',
    #'DESCRICAO_UPS',
    #'DATA_ALTERACAO_SMSA',
    #'VALOR_UPS_ANTIGA',
    #'DESCRICAO_UPS_ANTIGA',
    #'DESCRICAO_UPS',
    #'DESCRICAO_UPS_ANTIGA',
    #'DATA_HORA_BOLETIM',
    #'SEQUENCIAL_VEICULO',
    #'CODIGO_CATEGORIA',
    'DESCRICAO_CATEGORIA',
    #'CODIGO_ESPECIE',
    'DESCRICAO_ESPECIE',
    #'CODIGO_SITUACAO',
    'DESCRICAO_SITUACAO',
    #'TIPO_SOCORRO',
    #'DESCRICAO_TIPO_SOCORRO',
    #'No_BOLETIM',
    #'SEQ_VEIC',
    #'COD_CATEG',
    #'COD_ESPECIE',
    #'COD_SITUACAO',
    #'DESC_SITUACAO',
    #'DESC_TIPO_SOCORRO',
    'HORARIO',
    'DIA_SEMANA',
    'CENTRO-SUL'
    ]

    # Criar nova coluna HORARIO com base na hora informada (PICO 1/MANHÃ/TARDE/PICO 2/NOITE/MADRUGADA)
    dados['HORARIO'] = pd.to_datetime(dados['DATA HORA_BOLETIM'], format='%d/%m/%Y %H:%M').dt.hour
    dados['HORARIO'] = dados['HORARIO'].apply(lambda x: 'PICO 1' if 6 <= x < 9 else 'MANHÃ' if 9 <= x < 12 else 'TARDE' if 12 <= x < 16 else 'PICO 2' if 16 <= x < 19 else 'NOITE' if 19 <= x <= 23 else 'MADRUGADA')

    #Criar nova coluna DIA_SEMANA com base na DATA HORA_BOLETIM
    dados['DIA_SEMANA'] = pd.to_datetime(dados['DATA HORA_BOLETIM'], format='%d/%m/%Y %H:%M').dt.day_name()
    dados['DIA_SEMANA'] = dados['DIA_SEMANA'].replace(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], ['SEGUNDA-FEIRA', 'TERÇA-FEIRA', 'QUARTA-FEIRA', 'QUINTA-FEIRA', 'SEXTA-FEIRA', 'SÁBADO', 'DOMINGO'])

    dados['CENTRO-SUL'] = dados['COD_REGIONAL'].apply(lambda x: 1 if x == 19 else 0)

    # GERAR ARQUIVO PROPERTIES
    properties = dados[colunas_selecionadas]
    #Remova todas as linhas que tem alguma das colunas filtradas com valor vazio
    #properties = properties.dropna(subset=colunas_selecionadas)
    #Remova todas as linhas que tem alguma das colunas filtradas com valor NÃO INFORMADO
    #properties = properties[~properties.isin(['NÃO INFORMADO','NAO INFORMADO']).any(axis=1)]
    properties.to_csv('datasets/Acidentes/ocorridosCentroSul/properties.csv', index=False, sep='\t')

    # GERAR ARQUIVO QUALITIES
    qualities = dados[['CENTRO-SUL']]
    qualities.to_csv('datasets/Acidentes/ocorridosCentroSul/qualities.csv', index=False, sep='\t')

def gerar_entradas_acidentes_ocorridos_automoveis():
    dados = pd.read_csv('datasets/Acidentes/acidentes_veiculos_limpo.csv', low_memory=False, sep='\t')

    colunas_selecionadas = [
    #'NUMERO_BOLETIM',
    'DATA HORA_BOLETIM',
    #'NUMERO_BOLETIM',
    #'TIPO_ACIDENTE',
    'DESC_TIPO_ACIDENTE',
    #'COD_TEMPO',
    'DESC_TEMPO',
    #'COD_PAVIMENTO',
    'PAVIMENTO',
    #'COD_REGIONAL',
    #'DESC_REGIONAL',
    #'ORIGEM_BOLETIM',
    'LOCAL_SINALIZADO',
    #'VELOCIDADE_PERMITIDA',
    #'COORDENADA_X',
    #'COORDENADA_Y',
    #'HORA_INFORMADA',
    #'INDICADOR_FATALIDADE',
    #'VALOR_UPS',
    #'DESCRICAO_UPS',
    #'DATA_ALTERACAO_SMSA',
    #'VALOR_UPS_ANTIGA',
    #'DESCRICAO_UPS_ANTIGA',
    #'DESCRICAO_UPS',
    #'DESCRICAO_UPS_ANTIGA',
    #'DATA_HORA_BOLETIM',
    #'SEQUENCIAL_VEICULO',
    #'CODIGO_CATEGORIA',
    'DESCRICAO_CATEGORIA',
    #'CODIGO_ESPECIE',
    'DESCRICAO_ESPECIE',
    #'CODIGO_SITUACAO',
    'DESCRICAO_SITUACAO',
    #'TIPO_SOCORRO',
    #'DESCRICAO_TIPO_SOCORRO',
    #'No_BOLETIM',
    #'SEQ_VEIC',
    #'COD_CATEG',
    #'COD_ESPECIE',
    #'COD_SITUACAO',
    #'DESC_SITUACAO',
    #'DESC_TIPO_SOCORRO',
    'HORARIO',
    'DIA_SEMANA',
    'AUTOMOVEL'
    ]

    # Criar nova coluna HORARIO com base na hora informada (PICO 1/MANHÃ/TARDE/PICO 2/NOITE/MADRUGADA)
    dados['HORARIO'] = pd.to_datetime(dados['DATA HORA_BOLETIM'], format='%d/%m/%Y %H:%M').dt.hour
    dados['HORARIO'] = dados['HORARIO'].apply(lambda x: 'PICO 1' if 6 <= x < 9 else 'MANHÃ' if 9 <= x < 12 else 'TARDE' if 12 <= x < 16 else 'PICO 2' if 16 <= x < 19 else 'NOITE' if 19 <= x <= 23 else 'MADRUGADA')

    #Criar nova coluna DIA_SEMANA com base na DATA HORA_BOLETIM
    dados['DIA_SEMANA'] = pd.to_datetime(dados['DATA HORA_BOLETIM'], format='%d/%m/%Y %H:%M').dt.day_name()
    dados['DIA_SEMANA'] = dados['DIA_SEMANA'].replace(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], ['SEGUNDA-FEIRA', 'TERÇA-FEIRA', 'QUARTA-FEIRA', 'QUINTA-FEIRA', 'SEXTA-FEIRA', 'SÁBADO', 'DOMINGO'])

    dados['AUTOMOVEL'] = dados['DESCRICAO_SITUACAO'].apply(lambda x: 1 if x == 'AUTOMOVEL' else 0)

    # GERAR ARQUIVO PROPERTIES
    properties = dados[colunas_selecionadas]
    #Remova todas as linhas que tem alguma das colunas filtradas com valor vazio
    #properties = properties.dropna(subset=colunas_selecionadas)
    #Remova todas as linhas que tem alguma das colunas filtradas com valor NÃO INFORMADO
    #properties = properties[~properties.isin(['NÃO INFORMADO','NAO INFORMADO']).any(axis=1)]
    properties.to_csv('datasets/Acidentes/ocorridosAutomoveis/properties.csv', index=False, sep='\t')

    # GERAR ARQUIVO QUALITIES
    qualities = dados[['AUTOMOVEL']]
    qualities.to_csv('datasets/Acidentes/ocorridosAutomoveis/qualities.csv', index=False, sep='\t')

def gerar_entradas_acidentes_ocorridos_pico_tarde():
    dados = pd.read_csv('datasets/Acidentes/acidentes_veiculos_limpo.csv', low_memory=False, sep='\t')

    colunas_selecionadas = [
    #'NUMERO_BOLETIM',
    'DATA HORA_BOLETIM',
    #'NUMERO_BOLETIM',
    #'TIPO_ACIDENTE',
    'DESC_TIPO_ACIDENTE',
    #'COD_TEMPO',
    'DESC_TEMPO',
    #'COD_PAVIMENTO',
    'PAVIMENTO',
    #'COD_REGIONAL',
    #'DESC_REGIONAL',
    #'ORIGEM_BOLETIM',
    'LOCAL_SINALIZADO',
    #'VELOCIDADE_PERMITIDA',
    #'COORDENADA_X',
    #'COORDENADA_Y',
    #'HORA_INFORMADA',
    #'INDICADOR_FATALIDADE',
    #'VALOR_UPS',
    #'DESCRICAO_UPS',
    #'DATA_ALTERACAO_SMSA',
    #'VALOR_UPS_ANTIGA',
    #'DESCRICAO_UPS_ANTIGA',
    #'DESCRICAO_UPS',
    #'DESCRICAO_UPS_ANTIGA',
    #'DATA_HORA_BOLETIM',
    #'SEQUENCIAL_VEICULO',
    #'CODIGO_CATEGORIA',
    'DESCRICAO_CATEGORIA',
    #'CODIGO_ESPECIE',
    'DESCRICAO_ESPECIE',
    #'CODIGO_SITUACAO',
    'DESCRICAO_SITUACAO',
    #'TIPO_SOCORRO',
    #'DESCRICAO_TIPO_SOCORRO',
    #'No_BOLETIM',
    #'SEQ_VEIC',
    #'COD_CATEG',
    #'COD_ESPECIE',
    #'COD_SITUACAO',
    #'DESC_SITUACAO',
    #'DESC_TIPO_SOCORRO',
    'HORARIO',
    'DIA_SEMANA',
    'PICO_TARDE'
    ]

    # Criar nova coluna HORARIO com base na hora informada (PICO 1/MANHÃ/TARDE/PICO 2/NOITE/MADRUGADA)
    dados['HORARIO'] = pd.to_datetime(dados['DATA HORA_BOLETIM'], format='%d/%m/%Y %H:%M').dt.hour
    dados['HORARIO'] = dados['HORARIO'].apply(lambda x: 'PICO 1' if 6 <= x < 9 else 'MANHÃ' if 9 <= x < 12 else 'TARDE' if 12 <= x < 16 else 'PICO 2' if 16 <= x < 19 else 'NOITE' if 19 <= x <= 23 else 'MADRUGADA')

    #Criar nova coluna DIA_SEMANA com base na DATA HORA_BOLETIM
    dados['DIA_SEMANA'] = pd.to_datetime(dados['DATA HORA_BOLETIM'], format='%d/%m/%Y %H:%M').dt.day_name()
    dados['DIA_SEMANA'] = dados['DIA_SEMANA'].replace(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], ['SEGUNDA-FEIRA', 'TERÇA-FEIRA', 'QUARTA-FEIRA', 'QUINTA-FEIRA', 'SEXTA-FEIRA', 'SÁBADO', 'DOMINGO'])

    dados['PICO_TARDE'] = dados['HORARIO'].apply(lambda x: 1 if x == 'PICO 2' else 0)

    # GERAR ARQUIVO PROPERTIES
    properties = dados[colunas_selecionadas]
    #Remova todas as linhas que tem alguma das colunas filtradas com valor vazio
    #properties = properties.dropna(subset=colunas_selecionadas)
    #Remova todas as linhas que tem alguma das colunas filtradas com valor NÃO INFORMADO
    #properties = properties[~properties.isin(['NÃO INFORMADO','NAO INFORMADO']).any(axis=1)]
    properties.to_csv('datasets/Acidentes/ocorridosPicoTarde/properties.csv', index=False, sep='\t')

    # GERAR ARQUIVO QUALITIES
    qualities = dados[['PICO_TARDE']]
    qualities.to_csv('datasets/Acidentes/ocorridosPicoTarde/qualities.csv', index=False, sep='\t')

# MAIN
# gerar_csv_limpo(dados)
# gerar_entradas_acidentes_ocorridos()
# gerar_entradas_acidentes_ocorridos_centro_sul()
# gerar_entradas_acidentes_ocorridos_automoveis()
gerar_entradas_acidentes_ocorridos_pico_tarde()


'''

# Remover registros onde COORDENADA_X ou COORDENADA_Y são iguais a 0
# dados['COORDENADA_X'] = dados['COORDENADA_X'].astype(float)
# dados['COORDENADA_Y'] = dados['COORDENADA_Y'].astype(float)
# dados_filtrados = dados[(dados['COORDENADA_X'] != 0) & (dados['COORDENADA_Y'] != 0)]

dados_filtrados = dados[(dados['VELOCIDADE_PERMITIDA'] != 0)]
'''