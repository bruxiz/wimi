import unittest
import threading
import time
import requests
from app import app

class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app_thread = threading.Thread(target=app.run, kwargs={'host': '127.0.0.1', 'port': 5001, 'threaded': True})
        cls.app_thread.daemon = True
        cls.app_thread.start()
        time.sleep(1)

    def setUp(self):
        self.base_url = 'http://127.0.0.1:5001'

    def test_get_ip(self):
        response = requests.get(f'{self.base_url}/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.text.count('.') == 3)

if __name__ == '__main__':
    unittest.main()
