import sys

sys.path.append("..")

from fastapi import Depends, HTTPException, status, APIRouter
from pydantic import BaseModel
from typing import Optional
import models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError


SECRET_KEY = "8af02dc1f9988a3d8979820e4a679e0bca977d3e5488d8df33b2db6d8b7f2722"
ALGORITHM = "HS256"


class User(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str


bcrypt_context = CryptContext(schemes=["bcrypt"])

models.Base.metadata.create_all(bind=engine)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/auth", tags=["auth"], responses={401: {"user": "Not Authorized"}}
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def hash_password(password):
    return bcrypt_context.hash(password)


def verify_password(password, hashed_password):
    return bcrypt_context.verify(password, hashed_password)


def authenticate_user(username: str, password: str, db):
    user = db.query(models.Users).filter(models.Users.username == username).first()

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(
    username: str, id: int, expire_delta: Optional[timedelta] = None
):
    encode = {"sub": username, "id": id}
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minute=15)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        id: int = payload.get("id")
        if username is None or id is None:
            get_user_exception()
        return {"username": username, "id": id}
    except JWTError:
        raise get_user_exception()


@router.post("/user/create")
async def create_user(user: User, db: Session = Depends(get_db)):
    model = models.Users()
    model.username = user.username
    model.email = user.email
    model.first_name = user.first_name
    model.last_name = user.last_name
    password_hashed = hash_password(user.password)
    model.hashed_password = password_hashed
    model.is_active = True

    db.add(model)
    db.commit()

    return {"status": 201, "transaction": "Created Successfully"}


@router.post("/user/login")
async def login(
    form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(form.username, form.password, db)
    if not user:
        raise token_exception()
    token_expires = timedelta(minutes=20)
    token = create_access_token(user.username, user.id, expire_delta=token_expires)

    return {"token": token}


def get_user_exception():
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not valid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return credentials_exception


def token_exception():
    token_exception_response = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
