
# from pymongo.mongo_client import MongoClient 
# import os
# from dotenv import load_dotenv

# load_dotenv()

# MONGO_DB_URL=os.getenv("MONGODB_URL")

# uri =MONGO_DB_URL

# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


from bson import ObjectId
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://shoebahmed061:jS08Sh37LOtY2FjZ@cluster0.ge1cgjs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["Mlops"]
collection = db["ML"]
object_id = "675e59e762dd917a3532e6e6"
query = {"_id": ObjectId(object_id)}
document = collection.find()
if document:
    print(f"Document found: {document}")
else:
    print("Document not found or ObjectId is incorrect")

