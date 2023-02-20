from datetime import date
from pydantic import BaseModel, Field, EmailStr


class UserModel(BaseModel):
    first_name: str = Field(min_length=3, strict=True, max_length=30)
    second_name: str = Field(min_length=3, strict=True, max_length=50)
    email: EmailStr
    phone: str = Field(min_length=10, strict=True, max_length=13)
    birthaday: date
    description: str = Field(min_length=3, strict=True, max_length=250)


class UserResponse(UserModel):
    id: int = 1
    first_name: str = "User"
    second_name: str = "Example"
    email: EmailStr = "example@gmail.com"
    phone: str= "0987654321"
    birthaday: date = date(year=1988, month=3, day=25)
    description: str = "Created first contact for test"

    class Config:
        orm_mode = True