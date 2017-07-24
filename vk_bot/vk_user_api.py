import vk
from config import APP_ID, LOGIN, PASSWORD

session = vk.AuthSession(APP_ID, LOGIN, PASSWORD, scope='wall, messages, groups')
vk_user_api = vk.API(session)

def parse_posts(group_id):
    group_id = -int(group_id)
    posts = vk_user_api.wall.get(owner_id=group_id, count=3)
    if 'error' in posts:
        return [posts['error'], None]
    posts.remove(posts[0]) # removing request number, now "posts" really contain only posts.
    posts_to_send = []
    for post in posts:
        text = post['text']
        attachments_objects = []
        if 'attachments' in post:
            attachments = post['attachments']
            for attachment in attachments:
                attachment_object = make_attachment_object(attachment)
                if attachment_object:
                    attachments_objects.append(attachment_object)
        post_with_attachment = (text, attachments_objects)
        posts_to_send.append(post_with_attachment)
    return posts_to_send


def make_attachment_object(attachment):
    attachment_type = attachment['type']
    if attachment_type == 'link':
        return None
    id_name = attachment_type[0] + 'id'
    attachment_id = attachment[attachment_type][id_name]
    attachment_owner_id = attachment[attachment_type]['owner_id']
    if 'access_key' in attachment[attachment_type]:
        attachment_access_key = attachment[attachment_type]['access_key']
        attachments_object = '%s%s_%s_%s' % (
            attachment_type, attachment_owner_id, attachment_id, attachment_access_key)
    else:
        attachments_object = '%s%s_%s' % (attachment_type, attachment_owner_id, attachment_id)
    return attachments_object