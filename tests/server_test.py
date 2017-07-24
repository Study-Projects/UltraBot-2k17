from unittest import TestCase
from unittest.mock import patch, MagicMock
import os, json


from vk_bot import server


class MessageHandlersTestCase(TestCase):
    def setUp(self):
        self.TOKEN = 1
        self.user_info = 'USER_ID'

        server.app.config['TOKEN'] = self.TOKEN
        self.app = server.app.test_client()


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


    def generate_confirmation(self):
    	message_type = 'confirmation'
    	body = 'Doesn\'t matter'
    	return self.generate_vk_messaging_event(message_type, body)


    def generate_message_new(self, message):
        message_type = 'message_new'
        body = message
        return self.generate_vk_messaging_event(message_type, body)


    def generate_simple_message(self, message):
        return message


    @patch('vk_bot.server.message_handlers')
    def test_add_group_handler_gets_called(self, message_handlers_mock):
    	message_handlers_mock.add_group_handler = MagicMock()
    	vk_messaging_event = self.generate_message_new("Добавь мемогруппу memes memes")
    	self.app.post('/', data=json.dumps(vk_messaging_event))
    	number_of_calls = message_handlers_mock.add_group_handler.call_count
    	self.assertEqual(number_of_calls, 1)



    @patch('vk_bot.server.message_handlers')
    def test_delet_group_handler_gets_called(self, message_handlers_mock):
    	message_handlers_mock.add_group_handler = MagicMock()
    	vk_messaging_event = self.generate_message_new("Удали мемогруппу memes memes")
    	self.app.post('/', data=json.dumps(vk_messaging_event))
    	number_of_calls = message_handlers_mock.delete_group_handler.call_count
    	self.assertEqual(number_of_calls, 1)


    @patch('vk_bot.server.message_handlers')
    def test_post_handler_gets_called(self, message_handlers_mock):
    	message_handlers_mock.add_group_handler = MagicMock()
    	vk_messaging_event = self.generate_message_new("Пришли свежие мемы")
    	self.app.post('/', data=json.dumps(vk_messaging_event))
    	number_of_calls = message_handlers_mock.post_handler.call_count
    	self.assertEqual(number_of_calls, 1)


    @patch('vk_bot.server.message_handlers')
    def test_post_from_handler_gets_called(self, message_handlers_mock):
    	message_handlers_mock.add_group_handler = MagicMock()
    	vk_messaging_event = self.generate_message_new("Пришли новости из")
    	self.app.post('/', data=json.dumps(vk_messaging_event))
    	number_of_calls = message_handlers_mock.post_from_handler.call_count
    	self.assertEqual(number_of_calls, 1)


    @patch('vk_bot.server.message_handlers')
    def test_post_list_of_groups_handler_gets_called(self, message_handlers_mock):
        message_handlers_mock.add_group_handler = MagicMock()
        vk_messaging_event = self.generate_message_new("Пришли список новостигрупп")
        self.app.post('/', data=json.dumps(vk_messaging_event))
        number_of_calls = message_handlers_mock.post_list_of_groups_handler.call_count
        self.assertEqual(number_of_calls, 1)


    @patch('vk_bot.server.message_handlers')
    def test_delete_all_groups_handler_gets_called(self, message_handlers_mock):
        message_handlers_mock.add_group_handler = MagicMock()
        vk_messaging_event = self.generate_message_new("Удали все")
        self.app.post('/', data=json.dumps(vk_messaging_event))
        number_of_calls = message_handlers_mock.delete_all_groups_handler.call_count
        self.assertEqual(number_of_calls, 1)


    @patch('vk_bot.server.message_handlers')
    def test_post_weather_handler_gets_called(self, message_handlers_mock):
        message_handlers_mock.add_group_handler = MagicMock()
        vk_messaging_event = self.generate_message_new("Погода")
        self.app.post('/', data=json.dumps(vk_messaging_event))
        number_of_calls = message_handlers_mock.post_weather_handler.call_count
        self.assertEqual(number_of_calls, 1)              		    
    	
