from pydantic import BaseModel, EmailStr, Field

class Token(BaseModel):
    access_token: str = Field(default=None)
    token_type: str = Field(default=None)

class TokenData(BaseModel):
    username: str = Field(default=None)
    expire: int


class User(BaseModel):
    username: str = Field(default = None)
    password: str = Field(default=None)
    email: EmailStr = Field(default=None)
    full_name: str = Field(default=None)
    state: str = Field(default=None)
    isLogin: bool = False
    class Config:
        user_schema = {
            "user_demo":{
                "username" : "new",
                "password":"123",
                "email" :"patel@gmail.com",
                "full_name" : "Raghav Patel",
                "state": "Bihar",
            }
        }

class Device(BaseModel):
    name: str = Field(default=None)
    quantity: int = Field(default=1)
    description: str = Field(default=None)
    power_rated: int = Field(default=None)
    class Config:
        device_schema = {
            "user_demo":{
                "name" : "bulb",
                "quantity": 1,
                "description" : "kitchen bulb",
                "power_rated": 10,
            }
        }