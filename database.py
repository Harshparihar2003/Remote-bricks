from pymongo import MongoClient
import logging
import ssl


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# MongoDB connection
client = MongoClient("mongodb+srv://harsh9454696030:qLYZYlghHZS0UPzQ@cluster0.d93rs56.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.mydatabase


try:
    client = MongoClient(
        "mongodb+srv://harsh9454696030:qLYZYlghHZS0UPzQ@cluster0.d93rs56.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
        ssl=True,
    )
    db = client.mydatabase
    logger.info("Connected to MongoDB")
except Exception as e:
    logger.error(f"Error connecting to MongoDB: {e}")

def get_user_collection():
    return db.users

def get_details_collection():
    return db.details