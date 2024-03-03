
from fastapi import Depends
from db import get_db
from schema import UserSchema,TaskSchema


class Users:
    def register_user(users:UserSchema,db=Depends(get_db)):
        pass
        
    def login(email:str,password:str,db=Depends(get_db)):
        pass


class Tasks:
    def list_tasks(db=Depends(get_db)):
        pass

    def task_detail(task_id:int,db=Depends(get_db)):
        pass

    def add_task(tasks:TaskSchema,db=Depends(get_db)):
        pass

    def update_task(task_id:int,tasks:TaskSchema,db=Depends(get_db)):
        pass

    def delete_task(task_id:int,db=Depends(get_db)):
        pass



