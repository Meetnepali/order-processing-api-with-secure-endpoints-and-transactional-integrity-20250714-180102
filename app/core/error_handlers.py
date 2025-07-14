from fastapi.responses import JSONResponse
from fastapi import Request, status
from app.schemas import ErrorResponse

def generic_http_exception_handler(request: Request, exc: Exception):
    code = getattr(exc, "status_code", status.HTTP_400_BAD_REQUEST)
    detail = getattr(exc, "detail", str(exc))
    return JSONResponse(status_code=code, content=ErrorResponse(detail=detail).dict())
