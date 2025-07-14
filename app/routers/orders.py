from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.schemas import OrderCreate, OrderRead
from app.models import Order
from app.core.auth import get_current_user
from fastapi import HTTPException
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OrderRead, status_code=status.HTTP_201_CREATED)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    try:
        db.begin()
        new_order = Order(
            user_id=current_user['user_id'],
            product_name=order.product_name,
            quantity=order.quantity,
            total_amount=float(order.total_amount)
        )
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        return new_order
    except Exception as exc:
        db.rollback()
        raise HTTPException(status_code=400, detail="Order creation failed.") from exc

@router.get("/", response_model=List[OrderRead])
def list_orders(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    orders = db.query(Order).filter(Order.user_id == current_user['user_id']).order_by(Order.id.desc()).all()
    return orders
