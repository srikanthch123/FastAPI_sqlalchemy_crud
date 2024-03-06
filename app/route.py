from fastapi import APIRouter,Depends
from app.controller import Users,Tasks
from app.schema import UserSchema,TaskSchema
from app.db import get_db


login_router = APIRouter(tags=["Login"])

@login_router.post('/register-user')
async def register_user(users:UserSchema,db=Depends(get_db)):
    return Users.register_user(users,db)


@login_router.post('/login')
async def login(email:str,password:str,db=Depends(get_db)):
    return Users.login(email,password,db)



tasks_router = APIRouter(tags=["Tasks"])

@tasks_router.get('/list-tasks')
async def list_tasks(db=Depends(get_db)):
    return Tasks.list_tasks(db)

@tasks_router.get('/task-detail')
async def task_detail(task_id:int,db=Depends(get_db)):
    return Tasks.task_detail(task_id,db)

@tasks_router.post('/add-task')
async def add_task(tasks:TaskSchema,db=Depends(get_db)):
    return Tasks.add_task(tasks,db)

@tasks_router.put('/update-task')
async def update_task(task_id:int,tasks:TaskSchema,db=Depends(get_db)):
    return Tasks.update_task(task_id,tasks,db)

@tasks_router.delete('/delete-task')
async def delete_task(task_id:int,db=Depends(get_db)):
    return Tasks.delete_task(task_id,db)