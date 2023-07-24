import sys
from pathlib import Path


# Get the absolute path of the directory containing main.py
main_file = Path(__file__).resolve()
main_directory = main_file.parent

# Add the parent directory to the Python path
sys.path.append(str(main_directory.parent))


from fastapi import FastAPI
from database import engine
from routers import blog, user ,authentication
import models as models


app = FastAPI()

# Create database tables if they don't exist
models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)