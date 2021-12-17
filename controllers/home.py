from fastapi.exceptions import HTTPException
from fastapi import status

# from src.auth.base import JWT_SECRET, authenticate_user
from models.model import Users
from schemas.users import UserOutSchema, UserSubSchema

from tortoise.exceptions import IntegrityError


async def get_users_():
    return await UserOutSchema.from_queryset(Users.all())


async def create_users_(user):
    
    try:
        user_obj = Users(
            name=user.name,
            email=user.email,
        )
        await user_obj.save()
        return await UserOutSchema.from_tortoise_orm(user_obj)
        
    except IntegrityError as err:
        return f'There is a user with that email,please pick another. The error thrown is :{err}'


async def make_payment_(user: UserSubSchema, id):
    try:
        if True:
            new_status = 'premium'

        await Users.filter(id=id).update(subscription=new_status)
        return await Users.filter(id=id)
    except:
        print("there seems to be an error")




async def delete_user_(user_id):
    try:
        await Users.filter(id=user_id).delete()
        return f"The customer with id {user_id} has been deleted"
    except:
        print("there seems to be a user with that username")