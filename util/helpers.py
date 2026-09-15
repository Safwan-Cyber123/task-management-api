from SRC.util.db import getdb
from sqlalchemy.orm import Session
from SRC.user.models import UserModel
from fastapi import HTTPException,Request
from fastapi import Depends

from SRC.util.settings import settings

import jwt
from jwt.exceptions import InvalidTokenError

def is_auth(request:Request,db:Session=Depends(getdb)):
    try:
        token=request.headers.get("authorization")
        
        if not token:
          
          raise HTTPException(401,detail="You Are Unauthorized")
        token=token.split(" ")[-1]
        data=jwt.decode(token,settings.secret_key,settings.algo)
       
        user=db.query(UserModel).get(data.get("id"))
        if not user:
          raise HTTPException(401,detail="You Are Unauthorized")
        return user
    except InvalidTokenError:
      raise HTTPException(401,detail="You Are Unauthorized")