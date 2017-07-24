from unittest import TestCase
from unittest.mock import patch, MagicMock
import os


from vk_bot import server


class MessageHandlersTestCase(TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        pass   

		  
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
        body = 'Do some db action'
        return self.generate_vk_messaging_event(message_type, body)


    def generate_simple_message(self, message):
        return message


    def test_webhook(self):
    	pass