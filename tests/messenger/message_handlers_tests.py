from unittest import TestCase
from unittest.mock import patch, MagicMock


from vk_bot import server
from vk_bot.messenger import message_handlers


class MessageHandlersTestCase(TestCase):
	def setUp(self):
		self.user_info = "USER_ID"
		self.CONFIRMATION_TOKEN = '1'
		self.TOKEN = '1'
		server.app.config['CONFIRMATION_TOKEN'] = self.CONFIRMATION_TOKEN
		server.app.config['TOKEN'] = self.TOKEN
		



	def generate_vk_messaging_event(self, message_type, message):
		vk_messaging_event = {
			'type': message_type,
		    'object': {
				'user_id': self.user_info,
				'body': message
			}
		}
		return vk_messaging_event


	def generate_message_new(self):
		message_type = 'message_new'
		message = 'Doesn\'t matter'
		return self.generate_vk_messaging_event


	def test_add_group_handler(self):
		self.assertEqual(2,2)