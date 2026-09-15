from fastapi import FastAPI
from SRC.util.db import Base,engine
from SRC.task.models import TaskModel
from SRC.task.router import task_routers
from SRC.user.router import user_routers
Base.metadata.create_all(bind=engine)
app=FastAPI()
app.include_router(task_routers)
app.include_router(user_routers)

