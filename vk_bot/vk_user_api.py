import vk
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
            attachment_type = attachment['type']
            id_name = attachment_type[0] + 'id'
            attachment_id = attachment[attachment_type][id_name]
            attachment_owner_id = attachment[attachment_type]['owner_id']
            if 'access_key' in attachment[attachment_type]:
                attachment_access_key = attachment[attachment_type]['access_key']
                attachments_object = '%s%s_%s_%s' % (
                attachment_type, attachment_owner_id, attachment_id, attachment_access_key)
            else:
                attachments_object = '%s%s_%s' % (attachment_type, attachment_owner_id, attachment_id)
            attachments_objects.append(attachments_object)
    return text, attachments_objects
