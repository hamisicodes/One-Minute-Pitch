import unittest
from app.models import User,Comment,Pitch
from app import db

class TestComment(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username='James', password='potato', email='james@ms.com')
        self.new_pitch = Pitch(description = 'Hello flask', user = self.user_James)
        self.new_comment = Comment(description= 'Hello django' , user = self.user_James , pitch = self.new_pitch)


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.description,'Hello django')
        self.assertEquals(self.new_comment.user.username,'James')
        self.assertEquals(self.new_comment.pitch.description,'Hello flask')

