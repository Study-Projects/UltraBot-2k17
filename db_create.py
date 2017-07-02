from vk_bot.server import db
from vk_bot.models import groups

db.create_all()

db.session.add(News("top_news", "12345678"))

db.session.commit()


