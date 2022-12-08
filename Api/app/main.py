from fastapi import FastAPI
from router.router import user


app = FastAPI(
    title= "Streaming platform",
    description= "Netflix, Hulu, Amazon & Disney",
    version="2.0",
    openapi_tags=[{
        "name": "Querys",
        "description": "Streaming platform"
    }]
)

app.include_router(user)
