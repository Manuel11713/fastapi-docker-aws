from pydantic import BaseModel
from typing import Optional


class PaymentMethod(BaseModel):
    payment_id: str
    amount: int


class CheckoutOut(BaseModel):
    payment_id: str
