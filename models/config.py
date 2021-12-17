import os

databaseurl = "sqlite://access.db"

TORTOISE_ORM = {
    "connections": {"default": databaseurl},
    "apps": {
        "models": {
            "models": [
                "models.model", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}