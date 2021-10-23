import stripe
from config.settings import settings
stripe.api_key = settings.stripe_public_key


def stripe_create_payment_intent(payment_id: str, amount: int):
    try:
        stripe_res = stripe.PaymentIntent.create(
            amount=amount,
            currency="mxn",
            payment_method_types=["card"],
            payment_method=payment_id,
            confirm=True
        )
        return (200, stripe_res)
    except stripe.error.InvalidRequestError as err:
        return (400, {
            "ok": False,
            "message": str(err)
        })


# {
#   "id": "pi_3Jna6bL2LPuMe1xU0GNtojMh",
#   "object": "payment_intent",
#   "amount": 6000,
#   "amount_capturable": 0,
#   "amount_received": 6000,
#   "application": null,
#   "application_fee_amount": null,
#   "canceled_at": null,
#   "cancellation_reason": null,
#   "capture_method": "automatic",
#   "charges": {
#     "object": "list",
#     "data": [
#       {
#         "id": "ch_3Jna6bL2LPuMe1xU052Hnkr4",
#         "object": "charge",
#         "amount": 6000,
#         "amount_captured": 6000,
#         "amount_refunded": 0,
#         "application": null,
#         "application_fee": null,
#         "application_fee_amount": null,
#         "balance_transaction": "txn_3Jna6bL2LPuMe1xU0zb6VSzh",
#         "billing_details": {
#           "address": {
#             "city": null,
#             "country": null,
#             "line1": null,
#             "line2": null,
#             "postal_code": "12345",
#             "state": null
#           },
#           "email": null,
#           "name": null,
#           "phone": null
#         },
#         "calculated_statement_descriptor": "Stripe",
#         "captured": true,
#         "created": 1634956630,
#         "currency": "mxn",
#         "customer": null,
#         "description": null,
#         "destination": null,
#         "dispute": null,
#         "disputed": false,
#         "failure_code": null,
#         "failure_message": null,
#         "fraud_details": {},
#         "invoice": null,
#         "livemode": false,
#         "metadata": {},
#         "on_behalf_of": null,
#         "order": null,
#         "outcome": {
#           "network_status": "approved_by_network",
#           "reason": null,
#           "risk_level": "normal",
#           "risk_score": 47,
#           "seller_message": "Payment complete.",
#           "type": "authorized"
#         },
#         "paid": true,
#         "payment_intent": "pi_3Jna6bL2LPuMe1xU0GNtojMh",
#         "payment_method": "pm_1Jna5XL2LPuMe1xUzSqLWUPP",
#         "payment_method_details": {
#           "card": {
#             "brand": "visa",
#             "checks": {
#               "address_line1_check": null,
#               "address_postal_code_check": "pass",
#               "cvc_check": "pass"
#             },
#             "country": "US",
#             "exp_month": 4,
#             "exp_year": 2025,
#             "fingerprint": "bKJvT1U6lLdQuz6z",
#             "funding": "credit",
#             "installments": null,
#             "last4": "4242",
#             "network": "visa",
#             "three_d_secure": null,
#             "wallet": null
#           },
#           "type": "card"
#         },
#         "receipt_email": null,
#         "receipt_number": null,
#         "receipt_url": "https://pay.stripe.com/receipts/acct_1JauFXL2LPuMe1xU/ch_3Jna6bL2LPuMe1xU052Hnkr4/rcpt_KSV6NFYfRiqSN4bQAIieLyvOTFaxdrz",
#         "refunded": false,
#         "refunds": {
#           "object": "list",
#           "data": [],
#           "has_more": false,
#           "total_count": 0,
#           "url": "/v1/charges/ch_3Jna6bL2LPuMe1xU052Hnkr4/refunds"
#         },
#         "review": null,
#         "shipping": null,
#         "source": null,
#         "source_transfer": null,
#         "statement_descriptor": null,
#         "statement_descriptor_suffix": null,
#         "status": "succeeded",
#         "transfer_data": null,
#         "transfer_group": null
#       }
#     ],
#     "has_more": false,
#     "total_count": 1,
#     "url": "/v1/charges?payment_intent=pi_3Jna6bL2LPuMe1xU0GNtojMh"
#   },
#   "client_secret": "pi_3Jna6bL2LPuMe1xU0GNtojMh_secret_uMfUbjG1OQI9im83N5tmJBABA",
#   "confirmation_method": "automatic",
#   "created": 1634956629,
#   "currency": "mxn",
#   "customer": null,
#   "description": null,
#   "invoice": null,
#   "last_payment_error": null,
#   "livemode": false,
#   "metadata": {},
#   "next_action": null,
#   "on_behalf_of": null,
#   "payment_method": "pm_1Jna5XL2LPuMe1xUzSqLWUPP",
#   "payment_method_options": {
#     "card": {
#       "installments": null,
#       "network": null,
#       "request_three_d_secure": "automatic"
#     }
#   },
#   "payment_method_types": [
#     "card"
#   ],
#   "receipt_email": null,
#   "review": null,
#   "setup_future_usage": null,
#   "shipping": null,
#   "source": null,
#   "statement_descriptor": null,
#   "statement_descriptor_suffix": null,
#   "status": "succeeded",
#   "transfer_data": null,
#   "transfer_group": null
# }
