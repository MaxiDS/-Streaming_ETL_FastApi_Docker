#Modularizar o dividir nuestros routers
from fastapi import APIRouter
from config.db import engine
from models.user import streaming, cast_table, genre_table
from sqlalchemy import func, select


user = APIRouter()

#1-Máxima duración según tipo de film (película/serie), por plataforma y por año:
# El request debe ser: get_max_duration(año, plataforma, [min o season])

@user.get("/get_max_duration/{year}/{platform}/{tipo}", tags=["Querys"])
def get_max_duration(year:int,platform:str,tipo:str):
    with engine.connect() as conn:
        result = conn.execute(select(streaming.c.duration,streaming.c.title)
                            .where(streaming.c.release_year == year)
                            .where(streaming.c.platform==platform)
                            .where(streaming.c.type_duration==tipo)
                            .order_by(streaming.c.duration.desc())
                            )
        
        return result.first()
    
    
#2-Cantidad de películas y series (separado) por plataforma
#   El request debe ser: get_count_plataform(plataforma)

@user.get("/get_count_platform/{platform}", tags=["Querys"])
def get_count_platform(platform:str):
    with engine.connect() as conn:
        result = conn.execute(select(func.count(streaming.c.category).label("Cantidad"),streaming.c.category)                            
                            .where(streaming.c.platform==platform)
                            .group_by(streaming.c.category)
                            )
        
        return result.fetchall()
    

   
    
#3-Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
# El request debe ser: get_listedin('genero')
#Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 
# para la plataforma de amazon.   

@user.get("/get_listedin/{genre}", tags=["Querys"])
def get_listedin(genre:str):
    with engine.connect() as conn:
        result = conn.execute(select(streaming.c.platform,func.count(streaming.c.platform).label("Cantidad_repetidas"))
                            .join(genre_table,streaming.c.idStream==genre_table.c.idStream)
                            .where(genre_table.c.genre == genre)
                            .group_by(streaming.c.platform)
                            .order_by(func.count(streaming.c.platform).desc()) )
        
        return result.first()



#4-Actor que más se repite según plataforma y año.
#El request debe ser: get_actor(plataforma, año)

@user.get("/get_actor/{platform}", tags=["Querys"])
def get_actor(platform:str,year:int):
    with engine.connect() as conn:
        result = conn.execute(select(func.count(cast_table.c.cast).label("Cantidad_apariciones"),cast_table.c.cast)
                                    .join(streaming,streaming.c.idStream==cast_table.c.idStream)
                                    .where(streaming.c.release_year == year)
                                    .where(streaming.c.platform==platform)
                                    .where(cast_table.c.cast!="sin dato")
                                    .group_by(cast_table.c.cast)
                                    .order_by(func.count(cast_table.c.cast).desc()))
        
        return result.first()


