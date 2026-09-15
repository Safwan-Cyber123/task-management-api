from pydantic import BaseModel
class UserScheme(BaseModel):
        username:str
        email:str
        password:str
class UserResponseScheme(BaseModel):
        id:int
        username:str
        email:str
class UserLoginScheme(BaseModel):
      email:str
      password:str
        

