from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
import models
from database import engine
from routers import auth, todos, address

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(address.router)
