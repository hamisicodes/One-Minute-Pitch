from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer ,primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    pitches  = db.relationship('Pitch', backref = 'user' , lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read password')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer ,primary_key = True)
    name  = db.Column(db.String(255))
    category = db.Column(db.String(255), index = True)
    description = db.Column(db.String(255), index = True)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    user_id = db.Column(db.Integer , db.ForeignKey('users.id'))


    def save_pitch(self):
        def save_review(self):
            db.session.add(self)
            db.session.commit()

    @classmethod
    def get_pitches(cls):
        pitches = Pitch.query.all()
        return pitches


    

    def __repr__(self):
        return f'Post {self.name}'





