import pymongo

class Database:
    def __init__(self, connection_string: str, database_name: str):
        self.client = pymongo.MongoClient(connection_string)
        self.db = self.client[database_name]
        self.users = self.db["users"]
        
    def update_user(self, chat_id: int, user_id: int, level: int, points: int):
        self.users.update_one({"chat_id": chat_id, "user_id": user_id}, {"$set": {"level": level, "points": points}}, upsert=True)
        
    def get_user(self, chat_id: int, user_id: int):
        return self.users.find_one({"chat_id": chat_id, "user_id": user_id})
        
    def get_users_by_level(self, chat_id: int, level: int):
        return self.users.find({"chat_id": chat_id, "level": level})
