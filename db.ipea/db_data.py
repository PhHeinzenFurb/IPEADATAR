# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 21:02:02 2025

@author: Usuario
"""
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import pandas as pd
import ipeadatapy

# dados para acessar o PostgreSQL
usuario = "postgres"
senha = quote_plus("senha")  # Codifica o @ corretamente como %40
host = "localhost"
porta = "5432"
banco = "ipea"

# criando a egine de acesso ao PostgreSQL
engine = create_engine(f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}")

"""
Função para o tratamento dos dados de Demissão e Admissão sem ajuste do IPEA-CAGED

Códigos de referência: 
    - ADMISNC = Admissões
    - DESLIGNC = Demissões
    
Para gerar o df, utilziar o pacote ipeadatapy e a função timeseries()
    - ipeadatapy.timeseries("ADMISNC", year=2020)
"""
def prep_AdmiDemisaso(df):
    df = df[(df['NIVNOME'] == "Municípios") & (df["VALUE (Pessoa)"] != 0)]
    df = df.rename(columns={
        "VALUE (Pessoa)": "value",
        "RAW DATE": "raw_date"
    })
    df.columns = [col.lower() for col in df.columns]
    return df

# criando df para os dados de admissoes do ipea
df_admissoes = ipeadatapy.timeseries("ADMISNC", year=2020)

df_admissoes = prep_AdmiDemisaso(df_admissoes)


# inserindo dados dentro das tabelas criadas
#df_admissoes.to_sql("admissoesMunicipios", con=engine, if_exists="append", index=False)



















