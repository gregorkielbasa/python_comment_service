from fastapi import FastAPI

from controller.user.UserController import router as user_router

app = FastAPI()
app.include_router(user_router)

@app.get("/")
def hello_world() -> str:
    return "Hello World!"