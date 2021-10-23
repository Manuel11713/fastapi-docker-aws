from fastapi import APIRouter, Response
from schemas.checkout import PaymentMethod, CheckoutOut
from utils.stripe_utils import stripe_create_payment_intent

checkout_router = APIRouter()


@checkout_router.post("/", tags=['Checkout'])
def create_user(payment_method: PaymentMethod, response: Response):

    status, res = stripe_create_payment_intent(
        payment_method.payment_id, payment_method.amount
    )
    response.status_code = status

    return res
