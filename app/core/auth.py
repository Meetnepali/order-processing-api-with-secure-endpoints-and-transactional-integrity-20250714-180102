from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from typing import Optional

SECRET_KEY = "INSECURE-SECRET-KEY"
ALGORITHM = "HS256"
security = HTTPBearer()

# Dummy decode, expects token payload: { 'user_id': ... }
def decode_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token_payload = decode_token(credentials.credentials)
    if token_payload is None or 'user_id' not in token_payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    # Returns dict with user_id
    return token_payload
