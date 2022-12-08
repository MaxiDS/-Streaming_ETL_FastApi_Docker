from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:1234@host.docker.internal:3306/pi_henry_etl")

meta = MetaData()