import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))


from finticsai.app import app

class FinticsMlTestCase(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_get_asset(self):
        response = self.client.get('/assets/123')
        print(response.json)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
