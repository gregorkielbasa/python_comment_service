from fastapi import FastAPI
from starlette.responses import FileResponse
from controller.user.UserController import router as user_router
from controller.comment.CommentController import router as comment_router

app = FastAPI()
app.include_router(user_router)
app.include_router(comment_router)

# Serve index.html on root path
@app.get("/", response_class=FileResponse)
async def get_index():
    return "static/index.html"
