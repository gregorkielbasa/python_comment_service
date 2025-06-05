from fastapi import FastAPI

from controller.user.UserController import router as user_router
from controller.comment.CommentController import router as comment_router

app = FastAPI()
app.include_router(user_router)
app.include_router(comment_router)


@app.get("/")
def hello_world() -> str:
    return "Hello World!"
