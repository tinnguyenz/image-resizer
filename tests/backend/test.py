from unittest import TestCase
from photos_api import app
import unittest

class TestUpload(TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_upload(self):
        response = self.client.post(
            '/api/v1/upload',
            data={
                'file': (open('./tests/test_image.jpg', 'rb'), 'test_image.jpg')
            }
        )
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()