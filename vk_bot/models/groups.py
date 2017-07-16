from vk_bot.server import db

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_name = db.Column(db.String(128), unique=True, nullable=False)
    group_id = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, group_name, group_id):
        self.group_name = group_name
        self.group_id = group_id

    def __repr__(self):
        return '<News %r, %r>' % (self.group_name, self.group_id)


class Mems(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_name = db.Column(db.String(128), unique=True, nullable=False)
    group_id = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, group_name, group_id):
        self.group_name = group_name
        self.group_id = group_id

    def __repr__(self):
        return '<Mems %r, %r>' % (self.group_name, self.group_id)


