# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 17:59:36 2025

@author: Usuario
"""
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Integer, String, Column, SmallInteger, VARCHAR, ForeignKey
from urllib.parse import quote_plus

# dados para acessar o PostgreSQL
usuario = "postgres"
senha = quote_plus("senha")  # Codifica o @ corretamente como %40
host = "localhost"
porta = "5432"
banco = "ipea"

# criando a egine de acesso ao PostgreSQL
engine = create_engine(f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}")

# declarando a engine e criando a tabela
Base = declarative_base()

class ConsultaMunicipios(Base):
    __tablename__ = "dadosGeoMunicipios"
    code_muni = Column(Integer, primary_key=True)
    name_muni = Column(VARCHAR(200))
    code_state = Column(SmallInteger)
    abbrev_state = Column(String(2))
    name_state = Column(VARCHAR(30))
    code_region = Column(SmallInteger)
    name_region = Column(String(30))
    
class AdmissaoMunicipios(Base):
    __tablename__ = "admissoesMunicipios"
    id = Column(Integer, primary_key=True)
    code = Column(String(10))
    raw_date = Column(TIMESTAMP(timezone=True))
    tercodigo = Column(Integer, ForeignKey('dadosGeoMunicipios.code_muni'))
    year = Column(Integer)
    nivnome = Column(String(30))
    value = Column(Integer)

class DemissaoMunicipios(Base):
    __tablename__ = "demissoesMunicipios"
    id = Column(Integer, primary_key=True)
    code = Column(String(10))
    raw_date = Column(TIMESTAMP(timezone=True))
    tercodigo = Column(Integer, ForeignKey('dadosGeoMunicipios.code_muni'))
    year = Column(Integer)
    nivnome = Column(String(30))
    value = Column(Integer)
    

Base.metadata.create_all(engine)

# inserindo os dados dentro das tabelas dadosGeoMunicipios e 
# admissoes municipios


















