def is_add_group_command(messaging_event):
    validators = ['Добавь мемогруппу', 'Добавь новостигруппу']
    return validate(validators, messaging_event)


def is_delete_group_command(messaging_event):
    validators = ['Удали мемогруппу', 'Удали новостигруппу']
    return validate(validators, messaging_event)


def is_post_command(messaging_event):
    validators = ['Пришли свежие мемы', 'Пришли свежие новости']
    return validate(validators, messaging_event)


def is_post_from_command(messaging_event):
    validators = ['Пришли мемы из', 'Пришли новости из']
    return validate(validators, messaging_event)


def is_post_list_of_groups_command(messaging_event):
    validators = ['Пришли список мемогрупп', 'Пришли список новостигрупп']
    return validate(validators, messaging_event)


def is_parse_possible_photos_command(messaging_event):
    validators = ['Найди фото']
    return validate(validators, messaging_event)


def is_parse_hidden_info_command(messaging_event):
    validators = ['Найди инфо']
    return validate(validators, messaging_event)


def is_post_weather_command(messaging_event):
    validators = ['Погода']
    return validate(validators, messaging_event)


def is_help_command(messaging_event):
    validators = ['Помощь', 'Меню']
    return validate(validators, messaging_event)


def is_delete_all_groups_command(messaging_event):
    validators = ['Удали все']
    return validate(validators, messaging_event)


def validate(validators, messaging_event):
    for validator in validators:
        if validator in messaging_event:
            return True
    return False
