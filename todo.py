from fastapi import APIRouter,Path
from model import Name
from datetime import datetime


User_router = APIRouter()

name_list = []
name_counter = 0

@User_router.post("/user")
async def add_name(name:Name) -> dict:
    global name_counter
    name.id = name_counter = name_counter + 1
    name.created_at = datetime.now()
    name_list.append(name)

    return{
        "msg": "Insert success"
    }

@User_router.get("/user")
async def retrieve_todos() -> dict:
    return {
        "Users" : name_list
    }


@User_router.get("/user/{name_id}")
async def get_single_todo(name_id:int = Path(..., title="ID")) -> dict:
    for name in name_list:
        if name.id == name_id:
            return {
                "Users": name
            }
        
    return {"msg": "there is no task with the ID!"}   

@User_router.delete("/user/{name_id}")
async def delete_todo(name_id: int = Path(..., title="the ID of the todo to delete")) -> dict:
    for index,name in enumerate(name_list):
        if name.id == name_id:
            del name_list[index]
            return{"msg":f"User with ID {name_id} deleted successfully! ^^"}
    return {"msg": "User with supplied ID doesn't exist!"}     