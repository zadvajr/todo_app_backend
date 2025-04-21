from pymongo import MongoClient

client = MongoClient("mongodb+srv://zadva:2614Vara@cluster0.arxgrk2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.todo_db
collection_name = db["todo_collection"]