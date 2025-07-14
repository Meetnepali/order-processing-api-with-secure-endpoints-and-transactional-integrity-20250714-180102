from fastapi import FastAPI
from app.routers import orders
from app.core import error_handlers, auth
from app.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(orders.router, prefix='/orders', tags=["orders"])

app.add_exception_handler(Exception, error_handlers.generic_http_exception_handler)
