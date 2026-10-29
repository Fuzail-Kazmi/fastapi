from pydantic import BaseModel


class UserBase(BaseModel):
    name : str
    email : str


class CreateUser(UserBase):
    pass


class User(UserBase):
    id : int

    class config:
        from_attribute = True
