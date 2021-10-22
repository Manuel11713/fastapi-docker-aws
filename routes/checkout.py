from fastapi import APIRouter, Response
#from starlette.status import HTTP_204_NO_CONTENT
#from config.db import connection
#from models.user import userModel
from schemas.checkout import PaymentMethod, CheckoutOut
#from typing import List

checkout_router = APIRouter()


@checkout_router.post("/", response_model=CheckoutOut, tags=['Checkout'])
def create_user(payment_method: PaymentMethod):
    new_payment_method = {"payment_id": payment_method.payment_id,
                          "amount": payment_method.amount,
                          }
    print(new_payment_method)
    return new_payment_method
