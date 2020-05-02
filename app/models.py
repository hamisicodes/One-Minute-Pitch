from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer ,primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), index = True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    pitches  = db.relationship('Pitch' backref = 'user' , lazy = 'dynamic')

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer ,primary_key = True)
    name =  bio = db.Column(db.String(255))
    category = db.Column(db.String(255), index = True)
    description = db.Column(db.String(255), index = True)
    upvotes = db.Column(db.Integer
    downvotes = db.Column(db.Integer)
    user_id = db.Column(db.Integer , db.ForeignKey('users.id'))
    

    def __repr__(self):
        return f'Pitch {self.name}'


