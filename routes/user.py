from fastapi import APIRouter, Response
from starlette import status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import connection
from models.user import userModel
from schemas.user import User, UserOut
from utils.encrypt import encrypt_string
from typing import List

user = APIRouter()


@user.get("/", response_model=List[UserOut], tags=['User'])
def get_users():
    return connection.execute(userModel.select()).fetchall()


@user.get("/{id}", response_model=UserOut, tags=['User'])
def get_user(id: str):
    return connection.execute(userModel.select().where(userModel.c.id == id)).first()


@user.post("/", response_model=UserOut, tags=['User'])
def create_user(user: User):
    new_user = {"name": user.name,
                "email": user.email,
                "password": encrypt_string(user.password)
                }
    result = connection.execute(userModel.insert().values(new_user))
    new_user = connection.execute(userModel.select().where(
        userModel.c.id == result.lastrowid)).first()

    return new_user


@user.put("/{id}", response_model=UserOut, tags=['User'])
def update_user(id: str, user: User):
    connection.execute(
        userModel.update().values(
            name=user.name,
            email=user.email,
            password=encrypt_string(user.password)
        ).where(userModel.c.id == id)
    )
    return connection.execute(userModel.select().where(userModel.c.id == id)).first()


@user.delete("/{id}", status_code=HTTP_204_NO_CONTENT, tags=['User'])
def delete_user(id: str):
    connection.execute(userModel.delete().where(userModel.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)
