from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Task(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6, description="Must be between 1 to 5")
    complete: bool = Field(default=False)


@app.get("/task/")
async def task(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()


@app.get("/task/{id}/")
async def task_detail(id: int, db: Session = Depends(get_db)):
    model = db.query(models.Todos).filter(models.Todos.id == id).first()
    if model is not None:
        return model
    raise http_exception_404_not_found()


@app.post("/task")
async def create_task(task: Task, db: Session = Depends(get_db)):
    model = models.Todos()
    model.title = task.title
    model.description = task.description
    model.priority = task.priority
    model.complete = task.complete

    db.add(model)
    db.commit()

    return {"status": 201, "transaction": "Created Successfully"}


def http_exception_404_not_found():
    return HTTPException(status_code=404, detail="Task Not Found")
