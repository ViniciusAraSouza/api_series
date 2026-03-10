from fastapi import FastAPI
from app.database import engine
from app.models import serie
from app.route.serie import router

app = FastAPI()

serie.Base.metadata.create_all(bind=engine)

app.include_router(router)