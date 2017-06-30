import vk

session = vk.Session()
api = vk.API(session, v=5.0)


def send_message(user_id, token, message, attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id), message=message)


def get_user_info(letter_id):
    user_info = api.users.get(user_ids=letter_id)
    return user_info[0]


def get_user_id():
    pass


def get_group_id():
    pass


def parse_fresh_news():
    pass


def parse_fresh_memes():
    pass


def parse_possible_photos():
    pass


def parse_hidden_info():
    pass


def fetch_friends_list():
    pass


def fetch_groups_list():
    pass
