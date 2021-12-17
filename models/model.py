from tortoise import models
from tortoise import fields

class Users(models.Model):
    name = fields.CharField(200,null=True)
    email = fields.CharField(max_length=127, unique=True)
    subscription = fields.CharField(200, default="is_not_premium", null=True)
    
    def __str__(self):
        return self.name


