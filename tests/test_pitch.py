import unittest
from app.models import Pitch, User
from app import db

class TestPitch(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username='James', password='potato', email='james@ms.com')
        self.new_pitch = Pitch(description = 'Hello flask', user=self.user_James)


    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.description,'Helo flask')
        self.assertEquals(self.new_pitch.user.username,'James')

