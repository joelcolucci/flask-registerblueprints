import unittest

from tests.mock_app import app


class MockAppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_blueprint_one_is_registered(self):
        """Test blueprint one home page services"""
        response = self.app.get('/blueprint-one')

        self.assertTrue('Blueprint One' in response.data)

    def test_blueprint_two_is_registered(self):
        """Test blueprint two home page services"""
        response = self.app.get('/blueprint-two')

        self.assertTrue('Blueprint Two' in response.data)


if __name__ == '__main__':
    unittest.main()
