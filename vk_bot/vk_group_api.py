import vk

session = vk.Session()
vk_group_api = vk.API(session, v=5.0)


def send_message(user_id, token, message):
    vk_group_api.messages.send(access_token=token, user_id=str(user_id), message=message)


def get_user_info(user_letter_id):
    user_info = vk_group_api.users.get(user_ids=user_letter_id)
    if 'error' in user_info:
        return None
    return user_info[0]


def get_group_info(group_letter_id):
    group_info = vk_group_api.groups.getById(group_ids=group_letter_id)
    if 'error' in group_info:
        return None
    return group_info[0]['gid']


def fetch_friends_list(user_id):
    friends_list = vk_group_api.friends.get(user_id=user_id)
    if 'error' in friends_list:
        return None
    return friends_list['response']


def fetch_groups_list(user_id):
    groups_list = vk_group_api.groups.get(user_id=user_id)
    if 'error' in groups_list:
        return None
    return groups_list['response']
