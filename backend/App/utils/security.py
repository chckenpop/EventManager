from datetime import datetime, timedelta
from jose import jwt

ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,env.SECRET_KEY,algorithm = ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
    return payload