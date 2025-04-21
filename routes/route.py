from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schemas import todos_serializer, todo_serializer
from bson import ObjectId

router = APIRouter()

# GET Request Method 
@router.get("/")
async def get_todos():
    todos = todos_serializer(collection_name.find())
    return todos

# GET Request Method
@router.get("/{todo_id}")
async def get_todo_by_id(todo_id: str):
    todo = todo_serializer(collection_name.find_one(ObjectId(todo_id)))
    return todo

# POST Request Method
@router.post("/")
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))
    return {"message": "Todo added successfully!"}

# PUT Request Method
@router.put("/{todo_id}")
async def update_todo(todo_id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(todo_id)}, {"$set": dict(todo)})
    return {"message": "Todo updated successfully~"}

#DELETE Request Method
@router.delete("/{todo_id}")
async def delete_todo(todo_id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(todo_id)})
    return {"message": f"To do with id '{todo_id}' deleted successfully!"}