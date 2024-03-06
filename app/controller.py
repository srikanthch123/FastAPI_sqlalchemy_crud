from fastapi import Depends
from app.db import get_db
from app.schema import UserSchema,TaskSchema
from app.model import Task,User
from utils import GlobalHelper
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Users:
    def register_user(users:UserSchema,db=Depends(get_db)):
        try:
            users_data = users.dict() 
            users_data['password'] = pwd_context.hash(users.password)
            task = User(**users_data) 
            db.add(task)
            db.commit()
            return GlobalHelper.success_response(201,"New User Registerd","")
        except Exception as ex:
            return GlobalHelper.error_response(500,ex.args[0],"INTERNAL_SERVER_ERROR")

        
    def login(email:str,password:str,db=Depends(get_db)):
        pass


class Tasks:
    @staticmethod
    def list_tasks(db=Depends(get_db)):
        try:
            tasks = db.query(Task).all()
            return GlobalHelper.success_response(200,'Task List',tasks)
        except Exception as ex:
            return GlobalHelper.error_response(500,ex.args[0],"INTERNAL_SERVER_ERROR")
        
        
    @staticmethod
    def task_detail(task_id:int,db=Depends(get_db)):
        try:
            task=db.query(Task).filter(Task.id==task_id).first()
            if not task:
                return GlobalHelper.error_response(404,'Task id not found',"TASK_NOT_FOUND")
            else:
                return GlobalHelper.success_response(200,'Task details',task)
        except Exception as ex:
            return GlobalHelper.error_response(500,ex.args[0],"INTERNAL_SERVER_ERROR")

           
    @staticmethod    
    def add_task(tasks: TaskSchema, db=Depends(get_db)):
        try:
            task_data = tasks.dict() 
            task = Task(**task_data) 
            db.add(task)
            db.commit()
            return GlobalHelper.success_response(201,"New Task created","")
        except Exception as ex:
            return GlobalHelper.error_response(500,ex.args[0],"INTERNAL_SERVER_ERROR")
    

    @staticmethod
    def update_task(task_id:int,tasks:TaskSchema,db=Depends(get_db)):
        try:
            task = db.query(Task).filter(Task.id == task_id).first()
            if not task:
                return GlobalHelper.error_response(403,"Task not found","TASK_NOT_FOUND")
            task.title = tasks.title
            task.description = tasks.description
            task.bool = tasks.is_bool
            db.commit()
            return GlobalHelper.success_response(200,"Task updated","")
        except Exception as ex:
            return GlobalHelper.error_response(500,ex.args[0],"INTERNAL_SERVER_ERROR")

    @staticmethod
    def delete_task(task_id:int,db=Depends(get_db)):
        try:
            task = db.query(Task).filter(Task.id == task_id).first()
            if not task:
                return GlobalHelper.error_response(403,"Task not found","TASK_NOT_FOUND")
            db.delete(task)
            db.commit()
            return GlobalHelper.success_response(200,"Task deleted","")
        except Exception as ex:
            return GlobalHelper.error_response(500,ex.args[0],"INTERNAL_SERVER_ERROR")




