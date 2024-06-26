from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from todo import User_router
import uvicorn

app = FastAPI()

origins = ['http://127.0.0.1:5500', 'http://44.223.119.42/', 'http://44.223.119.42:8000/' , 'http://44.223.119.42:8002','http://44.223.119.42:8002/']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers =["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Welcome DY ! ^^"}

app.include_router(User_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8002,reload=True)

