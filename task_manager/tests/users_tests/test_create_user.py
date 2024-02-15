from task_manager.tools import TestCase, reverse_lazy
from task_manager.apps.users.models import User
from task_manager.settings import FIXTURE_DIRS
import json
import os


fixture_file_path = os.path.join(FIXTURE_DIRS[0], 'user.json')
with open(fixture_file_path) as fixture_file:
    test_user = json.load(fixture_file)


class CreateUserTest(TestCase):
    create_user_url = reverse_lazy('create_user')

    def test_create_user_page(self):
        response = self.client.get(self.create_user_url)
        self.assertEqual(response.status_code, 200)

    def test_user_creation_and_redirect(self):
        response = self.client.post(self.create_user_url, test_user)
        user = User.objects.get(pk=1)
        self.assertRedirects(response, reverse_lazy('login'))
        self.assertEqual(user.username, test_user.get('username'))
