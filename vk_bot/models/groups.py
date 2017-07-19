from vk_bot.server import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(128), nullable=False)
    mems_groups = db.relationship('Mems_group', backref='owner', lazy='dynamic')
    news_groups = db.relationship('News_group', backref='owner', lazy='dynamic')
        

class Mems_group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(128), unique=True, nullable=False)
    group_id = db.Column(db.String(128), unique=True, nullable=False)
    owner_id = db.Column(db.String, db.ForeignKey('user.user_id'))

    
class News_group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(128), unique=True, nullable=False)
    group_id = db.Column(db.String(128), unique=True, nullable=False)
    owner_id = db.Column(db.String, db.ForeignKey('user.user_id'))


