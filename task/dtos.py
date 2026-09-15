from pydantic import BaseModel
class TaskScheme(BaseModel):
    title:str
    Description:str
    is_complete:bool=False
class TaskResponseScheme(BaseModel):
    id:int
    title:str
    user_id:int|None=0
