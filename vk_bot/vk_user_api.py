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
    text = posts[1]['text']
    attachments_objects = []
    if 'attachments' in posts[1]:
        attachments = posts[1]['attachments']
        for attachment in attachments:
            if attachment['type'] == 'video':
                preview_id = attachment['video']['id']
                preview_owner_id = attachment['video']['owner_id']
                video = 'video%s_%s' % (preview_owner_id, preview_id)
                attachments_objects.append(video)
            if attachment['type'] == 'photo':
                photo_id = attachment['photo']['id']
                photo_owner_id = attachment['photo']['owner_id']
                photo = 'photo%s_%s' % (photo_owner_id, photo_id)
                attachments_objects.append(photo)
    return text, attachments_objects
