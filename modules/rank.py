from pyrogram import Client, filters
from pyrogram.types import Message
from database.database import Database

db = Database(config.MONGO_URI, config.MONGO_DB_NAME)
app = Client("my_bot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)

RANKS = [
    {"name": "Rank 1", "points": 0},
    {"name": "Rank 2", "points": 100},
    {"name": "Rank 3", "points": 200},
    {"name": "Rank 4", "points": 300},
    {"name": "Rank 5", "points": 400},
    # add more ranks here
]

# Define message handler
@app.on_message(filters.group)
def handle_message(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    points = db.get_user(chat_id, user_id).get("points", 0)
    level = get_level(points)

    if level > db.get_user(chat_id, user_id).get("level", 0):
        db.update_user(chat_id, user_id, level, points)
        rank_name = get_rank_name(level)
        client.send_message(chat_id, f"Congratulations, you have been promoted to {rank_name}!")
        
# Define command handler
@app.on_message(filters.command("me"))
def handle_me_command(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_data = db.get_user(chat_id, user_id)

    if user_data is None:
        client.send_message(chat_id, "You have not earned any points yet.")
    else:
        points = user_data["points"]
        level = user_data["level"]
        rank_name = get_rank_name(level)
        points_to_next_rank = get_points_to_next_rank(level, points)
        client.send_message(chat_id, f"Your current rank is {rank_name} ({points} points). {points_to_next_rank} points to next rank.")

def get_level(points: int) -> int:
    for i, rank in enumerate(RANKS):
        if points < rank["points"]:
            return i
    return len(RANKS)

def get_rank_name(level: int) -> str:
    return RANKS[level]["name"]

def get_points_to_next_rank(level: int, points: int) -> int:
    next_rank_points = RANKS[level + 1]["points"] if level + 1 < len(RANKS) else None
    if next_rank_points is None:
        return 0
    else:
        return next_rank_points - points
