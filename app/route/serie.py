from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.serie import SerieModel
from app.schemas.serie import SerieSchema

router = APIRouter(prefix="/series", tags=["Series"])


# LISTAR
@router.get("/")
def listar_series(db: Session = Depends(get_db)):
    return db.query(SerieModel).all()


# CRIAR
@router.post("/")
def criar_serie(serie: SerieSchema, db: Session = Depends(get_db)):
    nova_serie = SerieModel(
        titulo=serie.titulo,
        descricao=serie.descricao,
        ano_lancamento=serie.ano_lancamento
    )

    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)

    return nova_serie


# ATUALIZAR
@router.put("/{serie_id}")
def atualizar_serie(serie_id: int, serie: SerieSchema, db: Session = Depends(get_db)):

    serie_db = db.query(SerieModel).filter(SerieModel.id == serie_id).first()

    if not serie_db:
        raise HTTPException(status_code=404, detail="Série não encontrada")

    serie_db.titulo = serie.titulo
    serie_db.descricao = serie.descricao
    serie_db.ano_lancamento = serie.ano_lancamento

    db.commit()
    db.refresh(serie_db)

    return serie_db


# DELETAR
@router.delete("/{serie_id}")
def deletar_serie(serie_id: int, db: Session = Depends(get_db)):

    serie = db.query(SerieModel).filter(SerieModel.id == serie_id).first()

    if not serie:
        raise HTTPException(status_code=404, detail="Série não encontrada")

    db.delete(serie)
    db.commit()

    return {"message": "Série deletada com sucesso"}