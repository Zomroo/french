import config
from pymongo import MongoClient

class Database:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[config.COLLECTION_NAME]
        self.ensure_indexes()

    def ensure_indexes(self):
        try:
            self.collection.create_index([("chat_id", 1), ("user_id", 1)], unique=True)
        except ConnectionError as e:
            print(f"Failed to connect to database: {e}")

    def get_user(self, chat_id: int, user_id: int):
        return self.collection.find_one({"chat_id": chat_id, "user_id": user_id})

    def update_user(self, chat_id: int, user_id: int, level: int, points: int):
        self.collection.update_one(
            {"chat_id": chat_id, "user_id": user_id},
            {"$set": {"chat_id": chat_id, "user_id": user_id, "level": level, "points": points}},
            upsert=True
        )
