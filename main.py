from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from models.config import TORTOISE_ORM
from routes.home import router



Tortoise.init_models(["models.model"], "models")

app = FastAPI()

app.include_router(router)

register_tortoise(app=app, config=TORTOISE_ORM, generate_schemas=False)
