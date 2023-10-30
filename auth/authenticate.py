from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from auth.jwt import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

async def authenticate(token: str = Depends(oauth2_scheme)) -> str:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authenticated"
        )
    decode_token = verify_access_token(token)
    return decode_token["user"]
