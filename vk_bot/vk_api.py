import vk

session = vk.Session()
api = vk.API(session, v=5.0)


def send_message(user_id, token, message):
    api.messages.send(access_token=token, user_id=str(user_id), message=message)


def get_user_info(user_letter_id):
    user_info = api.users.get(user_ids=user_letter_id)
    if 'error' in user_info:
        return None
    return user_info[0]


def get_group_info(group_letter_id):
    group_info = api.groups.getById(group_ids=group_letter_id)
    if 'error' in group_info:
        return None
    return group_info[0]['id']


def fetch_friends_list(user_id):
    friends_list = api.friends.get(user_id=user_id)
    if 'error' in friends_list:
        return None
    return friends_list['response']


def fetch_groups_list(user_id):
    groups_list = api.groups.get(user_id=user_id)
    if 'error' in groups_list:
        return None
    return groups_list['response']


def parse_posts(is_user_posts, id):
    if not is_user_posts:
        id = '-' + str(id)
    posts = api.wall.get(owner_id=id)
    if 'error' in posts:
        return None
    return posts['response']
