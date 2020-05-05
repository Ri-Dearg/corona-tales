import unittest
from app import app


class BasicTestCase(unittest.TestCase):

    def test_story(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_fail(self):
        tester = app.test_client(self)
        response = tester.get('qwerty', content_type='html/text')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
