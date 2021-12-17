from pydantic.main import BaseModel
from models.model import Users
from tortoise.contrib.pydantic import pydantic_model_creator
from typing import Optional

# UserInSchema = pydantic_model_creator(
#     Managements_Research,
#     exclude_readonly=True
# )

UserOutSchema = pydantic_model_creator(
    Users,
    exclude_readonly=True
)

class UserInSchema(BaseModel):
    name : Optional[str]
    email : Optional[str]

class UserSubSchema(BaseModel):
    subscription : Optional[str]