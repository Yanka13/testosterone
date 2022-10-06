# tests/test_wsgi.py
from flask_testing import TestCase
from application import application

class TestViews(TestCase):
    def create_application(self):
        application.config['TESTING'] = True
        return application

    def test_one_roll(self):
        roll = self.client.get('/').json['roll']
        self.assertIsInstance(roll, int)
        self.assertGreater(roll, 0)
        self.assertLess(roll, 7)
