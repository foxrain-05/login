from fastapi import HTTPException, status
from jose import jwt, JWTError
from pydantic import EmailStr
from datetime import datetime


secret = 'rpNkSF259nFdyYKb6RZ6pbZn0F9kcfS6'

def create_access_token(user: EmailStr, exp: int):
    payload = {"user": user, "exp": exp}
    token = jwt.encode(payload, secret, algorithm="HS256")
    return token


def verify_access_token(token: str):
    try:
        data = jwt.decode(token, secret, algorithms="HS256")
        expires = data.get("expires")

        if expires is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="유효하지 않은 토큰입니다.",
            )
        
        # 토큰 만료 시간이 현재 시간보다 이전이면 토큰이 만료된 것으로 간주
        if datetime.utcnow() > datetime.fromtimestamp(expires):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="만료된 토큰입니다.",
            )
        return data
    
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="유효하지 않은 토큰입니다.",
        )