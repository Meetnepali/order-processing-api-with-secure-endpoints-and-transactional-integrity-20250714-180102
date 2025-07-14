from pydantic import BaseModel, PositiveInt, constr, condecimal
from typing import List

class OrderCreate(BaseModel):
    product_name: constr(min_length=1, max_length=100)
    quantity: PositiveInt
    total_amount: condecimal(gt=0, decimal_places=2)

class OrderRead(BaseModel):
    id: int
    product_name: str
    quantity: int
    total_amount: float

    class Config:
        orm_mode = True

class ErrorResponse(BaseModel):
    detail: str
