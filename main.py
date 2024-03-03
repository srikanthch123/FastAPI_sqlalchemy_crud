from fastapi import FastAPI
from route import login_router,tasks_router

app = FastAPI()

app.include_router(login_router)
app.include_router(tasks_router)



