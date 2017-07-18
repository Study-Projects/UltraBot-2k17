import vk
import os
from config import APP_ID, LOGIN, PASSWORD

session = vk.AuthSession(APP_ID, LOGIN, PASSWORD, scope='wall, messages, groups')
vk_user_api = vk.API(session)

def parse_posts(group_id):
    group_id = -int(group_id)
    posts = vk_user_api.wall.get(owner_id=group_id)
    if 'error' in posts:
        return None
    return posts[1]['id']