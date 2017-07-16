from vk_bot import server 
from flask_sqlalchemy import SQLAlchemy
import os

server.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
server.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(server.app)

