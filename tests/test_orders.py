import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core import auth
import time
from jose import jwt

client = TestClient(app)
SECRET_KEY = auth.SECRET_KEY
ALGORITHM = auth.ALGORITHM

def create_jwt(user_id):
    payload = {"user_id": user_id}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def test_unauthorized_user_cannot_access_orders():
    # No Authorization header
    resp = client.get("/orders/")
    assert resp.status_code == 401
    assert "detail" in resp.json()

    order = {"product_name": "item", "quantity": 2, "total_amount": "22.50"}
    resp2 = client.post("/orders/", json=order)
    assert resp2.status_code == 401
    assert "detail" in resp2.json()

def test_invalid_order_input_is_rejected():
    token = create_jwt(999)
    headers = {"Authorization": f"Bearer {token}"}
    invalid_order = {"product_name": "", "quantity": 0, "total_amount": "0.00"}
    resp = client.post("/orders/", json=invalid_order, headers=headers)
    # Expect 422 from FastAPI's validation
    assert resp.status_code == 422
    assert "detail" in resp.json()
