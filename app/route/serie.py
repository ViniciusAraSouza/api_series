from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.serie import SerieModel
from app.schema.serie import SerieSchema

serie = APIRouter()

@serie.post("/")
async def cria_serie(dados: SerieSchema, db: Session = Depends (get_db)):
    nova_serie = SerieModel(**dados.model_dump())
    db.add(nova_serie)  
    db.commit()
    db.refresh(nova_serie)
    return nova_serie

@serie.get("/series")
async def liosyar_series(db: Session = Depends (get_db)):
    return db.query(SerieModel).all()



# Tarefa 1: Crie as rota de atualização e deleção da API
# Tarefa 2: Crie as noavas rotas de atualização e deleção da API
# Tarefa 3: Resolva todos os erros das novas rotas
# Versione 

# Extra: resolva o erro de importação das variáveis de ambiente detectado np módulo pyhton-dotenv e ultilize corretamente a importação com a função load_dotenv() em seu database.py
