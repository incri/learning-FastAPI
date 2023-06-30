from fastapi import FastAPI
from database import engine
import schemas ,models

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post('/blog')
def create(blog : schemas.Blog):
    return blog
