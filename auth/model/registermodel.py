from pydantic import BaseModel

class RegisterModel(BaseModel):
    fullname: str
    nickname:str
    email: str
    password: str