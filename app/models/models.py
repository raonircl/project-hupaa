from tortoise import fields, models
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(models.Model):
    id = fields.IntField(pk=true)
    username = fields.CharField(max_length=50, unique=true)
    email = fields.CharField(max_length=100, unique=true)
    hashed_password = fields.CharField(max_length=128)
    is_active = fields.BooleanField(default=false)
    photo = fields.CharField(max_length=255, null=true)

    def verify_password(self, password: str):
        return pwd_context.verify(password, self.hashed_password)
    
    def set_password(self, password: str):
        self.hashed_password = pwd_context.hash(password)