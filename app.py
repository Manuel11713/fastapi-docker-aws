from fastapi import FastAPI
from routes.user import user
from routes.checkout import checkout_router


app = FastAPI(
    title="My first API",
    description="this is my first api with fastapi",
    version="0.0.1",
    openapi_tags=[{
        "name": "User",
        "description": "this is the description for user routes"
    }])

app.include_router(user, prefix="/users")
app.include_router(checkout_router, prefix="/checkout")
