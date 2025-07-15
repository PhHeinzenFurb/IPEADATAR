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

# filtrando apenas os municipios
#df_admissoes = df_admissoes[(df_admissoes['NIVNOME'] == "Municípios") & (df_admissoes["VALUE (Pessoa)"] != 0 )]

# renomeando as colunas
#df_admissoes = df_admissoes.rename(columns={
#    "VALUE (Pessoa)": "value",
#    "RAW DATE": "raw_date"
#    })

# colocando colunas em caixa baixa
#df_admissoes.columns = [col.lower() for col in df_admissoes.columns]

# criando df para os dados de demissoes
#df_demissoes = ipeadatapy.timeseries("DESLIGNC")

# filtrando apenas os municipios
# = df_demissoes[(df_demissoes['NIVNOME'] == "Municípios") & (df_demissoes["VALUE (Pessoa)"] != 0 )]

# renomeando as colunas
#df_demissoes = df_demissoes.rename(columns={
#    "VALUE (Pessoa)": "value",
#    "RAW DATE": "raw_date"
#    })

# colocando colunas em caixa baixa
#df_demissoes.columns = [col.lower() for col in df_demissoes.columns]



# inserindo dados dentro das tabelas criadas
#df_admissoes.to_sql("admissoesMunicipios", con=engine, if_exists="append", index=False)
#df_demissoes.to_sql("demissoesMunicipios", con=engine, if_exists="append", index=False)


















