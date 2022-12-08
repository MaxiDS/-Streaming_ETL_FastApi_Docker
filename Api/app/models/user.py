from sqlalchemy import Table, Column 
from sqlalchemy.types import Integer, String
from config.db import engine, meta 

streaming = Table("streaming",meta,
            Column("idStream", String(30)) ,
            Column("category", String(50)),
            Column("title", String(120)) ,
            Column("release_year", Integer),
            Column("duration", Integer) ,
            Column("type_duration", String(20)) ,
            Column("platform", String(20)) )



cast_table = Table("cast_table",meta,
            Column("idStream", String(30)) ,
            Column("cast", String(120)),
           )


genre_table = Table("genre_table",meta,
            Column("idStream", String(30)) ,
            Column("genre", String(120)),
           )



meta.create_all(engine)