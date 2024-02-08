from task_manager import SimpleTestCase


class HomepageTest(SimpleTestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
