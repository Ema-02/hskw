from pyrogram import Client
import pyromod
# @BENN_DEV & @BENfiles

api_id = 23337074
api_hash = "2e0ea05d6d6bfd6708fa51f54f36baf7"
bot_token = "6497717567:AAF_qXfKRegCOSJjiJHVdTjt7bCskuYwuoQ"


app = Client(
    name = "MediaDownloader", 
    api_id = api_id, 
    api_hash = api_hash, 
    bot_token = bot_token,
    in_memory=True, 
    plugins=dict(root="Bot/handlers")
)
