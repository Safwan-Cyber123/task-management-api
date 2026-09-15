from SRC.user.dtos import UserScheme,UserLoginScheme
from sqlalchemy.orm import Session
from SRC.user.models import UserModel
from fastapi import HTTPException,Request,BackgroundTasks
from pwdlib import PasswordHash
from SRC.util.settings import settings
from SRC.util.mail import sendemail
from datetime import datetime,timedelta
import jwt
from jwt.exceptions import InvalidTokenError
password_hash=PasswordHash.recommended()
def get_hash_key(password):
    return password_hash.hash(password)
def verify_password(plain_password,hashed_password):
     return password_hash.verify(plain_password,hashed_password)
async def register(body:UserScheme,db:Session,bg_task:BackgroundTasks):
    is_user=db.query(UserModel).filter(UserModel.username==body.username).first()
    if is_user:
        raise HTTPException(400,detail="User Already Exist")
    is_user=db.query(UserModel).filter(UserModel.email==body.email).first()
    if is_user:
        raise HTTPException(400,detail="User Already Exist")

    hash_key=get_hash_key(body.password)
    new_user=UserModel(username=body.username,email=body.email,hashed_password=hash_key)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    bg_task.add_task(sendemail, [new_user.email])
    return new_user
def login (body:UserLoginScheme,db:Session):
    is_user=db.query(UserModel).filter(UserModel.email==body.email).first()
    if not is_user:
            raise HTTPException(401,detail="Incorrect Credentals")
    
    if not verify_password(body.password,is_user.hashed_password):
         raise HTTPException(401,detail="Invalid Credenrial")
    exp_time=datetime.now()+timedelta(minutes=settings.exp_time)
    token=jwt.encode({"id":is_user.id,"exp":exp_time.timestamp()},settings.secret_key,settings.algo)
    return {"token":token}




 
         
     
     