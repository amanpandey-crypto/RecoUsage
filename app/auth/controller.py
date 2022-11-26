from datetime import datetime, timedelta
from typing import Union
import time
from fastapi import HTTPException, status, Depends
from jose import JWTError, jwt
from passlib.context import CryptContext
from decouple import config
from database.model import Token, TokenData, User
from database.setup import session_info

# to get a string like this run:
# openssl rand -hex 32

SECRET_KEY = config("secret")
ALGORITHM = config("algo")

ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY , algorithm= ALGORITHM)
    return encoded_jwt


def validate_token(token):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="This token is expired. You need to log in again.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = decoded_token.get("sub")
        if decoded_token["exp"] >= time.time():
            return decoded_token
        else:
            session_info.delete_one({"username": username})
            raise credentials_exception
    except JWTError:
        return {}
