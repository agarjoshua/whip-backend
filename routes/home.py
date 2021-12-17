from typing import List
from fastapi import APIRouter
# import all the schemas
from schemas.users import UserInSchema,UserOutSchema, UserSubSchema

#import all controllers
from controllers.home import create_users_, delete_user_, get_users_, make_payment_

router = APIRouter(tags=["Home"])

@router.get(
    "/get_users",
    # response_model=UserOutSchema
)
async def get_users():
    return await get_users_()


@router.post(
    "/create_users",
    # response_model=PropertyInSchema
)

async def create_properties(prop: UserInSchema):
    return await create_users_(prop)

@router.patch(
    "/make_payment",
    # response_model=UserOutSchema
)
async def make_payment(user: UserSubSchema,id):
    return await make_payment_(user,id)

@router.delete(
    "/delete_user",
    response_model=UserOutSchema
)
async def delete_property(id):
    return await delete_user_(id)