import os

class Config(object):
    BOT_TOKEN = os.environ.get("")
    API_ID = int(os.environ.get("22470912"))
    API_HASH = os.environ.get("511be78079ed5d4bd4c967bc7b5ee023")
    VIP_USER = os.environ.get('VIP_USERS', '7678862761').split(',')
    VIP_USERS = [int() for user_id in VIP_USER]
