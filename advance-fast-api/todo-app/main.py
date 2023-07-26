from fastapi import FastAPI, Depends, HTTPException
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/task/")
async def task(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()


@app.get("/task/{id}/")
async def task_detail(id: int, db: Session = Depends(get_db)):
    model = db.query(models.Todos).filter(models.Todos.id == id).first()
    if model is not None:
        return model
    raise http_exception_404_not_found()


def http_exception_404_not_found():
    return HTTPException(status_code=404, detail="Task Not Found")
