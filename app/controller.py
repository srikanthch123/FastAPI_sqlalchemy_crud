from fastapi import HTTPException,status
from fastapi import Depends
from app.db import get_db
from app.schema import UserSchema,TaskSchema
from app.model import Task,User


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

    def add_task(tasks: TaskSchema, db=Depends(get_db)):
        try:
            task_data = tasks.dict() 
            task = Task(**task_data) 
            db.add(task)
            db.commit()
            return {"message": "Task created"}
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

    def update_task(task_id:int,tasks:TaskSchema,db=Depends(get_db)):
        pass

    def delete_task(task_id:int,db=Depends(get_db)):
        pass



