import vk
import os
from config import APP_ID, LOGIN, PASSWORD

session = vk.AuthSession(APP_ID, LOGIN, PASSWORD, scope='wall, messages, groups')
vk_user_api = vk.API(session, v=5.0)

def parse_posts(group_id):
    group_id = -int(group_id)
    posts = vk_user_api.wall.get(owner_id=group_id)
    if 'error' in posts:
        return None
    text = posts[1]
    attachments_objects = []
    if 'attachments' in posts[1]:
        attachments = posts[1]['attachments']
        for attachment in attachments:
                attachment_type = attachment['type']
                attachment_id = attachment[attachment_type]['id']
                attachment_owner_id = attachment[attachment_type]['owner_id']
                attachments_object = '%s%s_%s' % (attachment_type, attachment_id, attachment_owner_id)
                attachments_objects.append(attachments_object)
    return text, attachments_objects
