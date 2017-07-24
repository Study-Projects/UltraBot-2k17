from unittest import TestCase
from unittest.mock import patch, MagicMock
import os


from vk_bot import server
from vk_bot.messenger import message_handlers
from vk_bot.models.groups import User, News_group, Mems_group
from config import basedir


class MessageHandlersTestCase(TestCase):
    def setUp(self):
        self.user_info = "USER_ID"
        self.TOKEN = '1'
        self.WEATHER_KEY = '1'
        server.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        server.db.create_all()


    def tearDown(self):
        server.db.session.remove()
        server.db.drop_all()   

		  
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


    
    @patch('vk_bot.messenger.message_handlers.is_memes_group')
    @patch('vk_bot.messenger.message_handlers.vk_group_api.send_message')
    def test_add_group_handler(self, send_message_mock, is_memes_group_mock):
        vk_messaging_event = self.generate_message_new()
        vk_response = vk_messaging_event['object']['body']
        user_info = vk_messaging_event['object']['user_id']
        user_id = User.query.get(1)
        self.assertEqual(user_id, None)
        user_id = User(user_id=str(user_info))
        server.db.session.add(user_id)
        server.db.session.commit()
        self.assertEqual(user_id, User.query.get(1))
        message_handlers.add_group_handler(user_info, self.TOKEN, vk_response)
        message = self.generate_simple_message(message="Группа добавлена")
        send_message_mock.assert_called_once_with(user_info, self.TOKEN, message)


    @patch('vk_bot.messenger.message_handlers.is_memes_group')
    @patch('vk_bot.messenger.message_handlers.vk_group_api.send_message')
    def test_delete_group_handler(self, send_message_mock, is_memes_group_mock):
        vk_messaging_event = self.generate_message_new()
        vk_response = vk_messaging_event['object']['body']
        user_info = vk_messaging_event['object']['user_id']
        user_id = User.query.get(1)
        self.assertEqual(user_id, None)
        user_id = User(user_id=str(user_info))
        server.db.session.add(user_id)
        server.db.session.commit()
        self.assertEqual(user_id, User.query.get(1))
        message_handlers.delete_group_handler(user_info, self.TOKEN, vk_response)
        message = self.generate_simple_message(message="Список групп пуст")
        send_message_mock.assert_called_once_with(user_info, self.TOKEN, message)


    @patch('vk_bot.messenger.message_handlers.vk_group_api.send_message')    
    def test_post_handler(self, send_message_mock):
        vk_messaging_event = self.generate_message_new()
        vk_response = vk_messaging_event['object']['body']
        user_info = vk_messaging_event['object']['user_id']
        user_id = User.query.get(1)
        self.assertEqual(user_id, None)
        user_id = User(user_id=str(user_info))
        server.db.session.add(user_id)
        server.db.session.commit()
        message_handlers.post_handler(user_info, self.TOKEN, vk_response)
        message = self.generate_simple_message(message="Не понял тип поста")
        send_message_mock.assert_called_once_with(user_info, self.TOKEN, message)


    @patch('vk_bot.messenger.message_handlers.vk_group_api.send_message')    
    def test_post_from_handler(self, send_message_mock):
        vk_messaging_event = self.generate_message_new()
        vk_response = vk_messaging_event['object']['body']
        user_info = vk_messaging_event['object']['user_id']
        user_id = User.query.get(1)
        self.assertEqual(user_id, None)
        user_id = User(user_id=str(user_info))
        server.db.session.add(user_id)
        server.db.session.commit()
        message_handlers.post_from_handler(user_info, self.TOKEN, vk_response)
        message = self.generate_simple_message(message="Не понял тип поста")
        send_message_mock.assert_called_once_with(user_info, self.TOKEN, message)


    @patch('vk_bot.messenger.message_handlers.vk_group_api.send_message')    
    def test_post_list_of_groups_handler(self, send_message_mock):
        vk_messaging_event = self.generate_message_new()
        vk_response = vk_messaging_event['object']['body']
        user_info = vk_messaging_event['object']['user_id']
        user_id = User.query.get(1)
        self.assertEqual(user_id, None)
        user_id = User(user_id=str(user_info))
        server.db.session.add(user_id)
        server.db.session.commit()
        message_handlers.post_list_of_groups_handler(user_info, self.TOKEN, vk_response)
        message = self.generate_simple_message(message="Не понял тип поста")
        send_message_mock.assert_called_once_with(user_info, self.TOKEN, message)


    @patch('vk_bot.messenger.message_handlers.vk_group_api.send_message')    
    def test_delete_all_groups_handler(self, send_message_mock):
        vk_messaging_event = self.generate_message_new()
        vk_response = vk_messaging_event['object']['body']
        user_info = vk_messaging_event['object']['user_id']
        user_id = User.query.get(1)
        self.assertEqual(user_id, None)
        user_id = User(user_id=str(user_info))
        server.db.session.add(user_id)
        server.db.session.commit()
        message_handlers.delete_all_groups_handler(user_info, self.TOKEN, vk_response)
        message = self.generate_simple_message(message="Не понял тип групп")
        send_message_mock.assert_called_once_with(user_info, self.TOKEN, message)


    @patch('vk_bot.messenger.message_handlers.weather_api.fetch_weather')
    @patch('vk_bot.messenger.message_handlers.vk_group_api.send_message')    
    def test_post_weather_handler(self, send_message_mock, fetch_weather_mock):
        vk_messaging_event = self.generate_message_new()
        vk_response = vk_messaging_event['object']['body']
        user_info = vk_messaging_event['object']['user_id']
        city = vk_response.split()[-1]
        weather_info = fetch_weather_mock(self.WEATHER_KEY, city)
        fetch_weather_mock.assert_called_once_with(self.WEATHER_KEY, city)
        message_handlers.post_weather_handler(user_info, self.TOKEN, vk_response)
        send_message_mock.assert_called_once_with(user_info, self.TOKEN, weather_info)









                

