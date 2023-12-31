from fastapi import FastAPI
from routes.user import router as user_router

app = FastAPI()
app.include_router(user_router, tags=["user"], prefix="/api/user")

@app.get("/")
async def read_root():
    return {"Hello": "World"}













