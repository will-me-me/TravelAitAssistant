import pymongo
from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["TravelDb"]
    
    # Test the connection
    client.admin.command('ping')
    print("✅ Connected to MongoDB successfully!")
    
    # You can now use your database
    collection = db["TravelCollection"]
    
except Exception as e:
    print(f"❌ Connection failed: {e}")