from unittest import TestCase
from unittest.mock import patch, MagicMock


from vk_bot import server
from vk_bot.messenger import message_handlers


class MessageHandlersTestCase(TestCase):
    def setUp(self):
    self.user_info = "USER_ID"
	self.CONFIRMATION_TOKEN = '1'
	self.TOKEN = '1'
		
		
    def generate_vk_messaging_event(self, message_type, body):
        vk_messaging_event = {
            'type': message_type,
            'object': {
                'user_id': self.user_info,
                'body': body
	    }
	}
	return vk_messaging_event


    def generate_message_new(self):
        message_type = 'message_new'
        body = 'Make some message action'
        return self.generate_vk_messaging_event(message_type, body)


    def generate_simple_message(self, message):
        return message


    @patch('vk_bot.messenger.message_handlers.vk_group_api.send_message')
    @patch('vk_bot.messenger.message_handlers.User')
    def test_add_group_handler(self, user, send_message_mock):
        vk_messaging_event = self.generate_message_new()
        vk_response = vk_messaging_event['object']['body']
        user_info = vk_messaging_event['object']['user_id']
        user_id = MagicMock(user_info)
        message = self.generate_simple_message(message="Не понял тип группы")
        message_handlers.add_group_handler(user_info, self.TOKEN, vk_response)
        send_message_mock.assert_called_once_with(user_info, self.TOKEN, message)
 
