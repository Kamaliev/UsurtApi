from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from starlette import status
from schema.auth import TokenData

route = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = '9d74e2dac88e24908672fcde8bcf2518ca4c0b2744ae48eb512bf4442c5b4b2a '
ALGORITHM = "HS256"


def create_token(data: dict):
    jwt_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token


async def auth(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username


@route.post("/token", response_model=TokenData)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = form_data.username
    access_token = create_token({"sub": user})
    return TokenData(token=access_token, type='Bearer')

if __name__ == '__main__':
    import requests

    r = requests.post('http://127.0.0.1:8000/token', data={'username': '123', 'password': 'sdadadsad'})
    print(r.text)