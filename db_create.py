from vk_bot.models.base import db
from vk_bot.models.groups import News

db.create_all()

db.session.add(News("top_news", "12345678"))

db.session.commit()


