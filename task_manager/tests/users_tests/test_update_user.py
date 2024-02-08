from task_manager import TransactionTestCase, reverse_lazy
from task_manager.users.models import User
from task_manager.settings import FIXTURE_DIRS
import json
import os


fixture_file_path = os.path.join(FIXTURE_DIRS[0], 'user.json')
with open(fixture_file_path) as fixture_file:
    TEST_USER = json.load(fixture_file)


class UpdateUserTest(TransactionTestCase):
    fixtures = ['database.json']
    username = TEST_USER.get('username')

    def test_only_logged_user_can_update(self):
        response = self.client.post(
            reverse_lazy('update_user', kwargs={'pk': 1}),
            TEST_USER,
        )
        self.assertRedirects(response, reverse_lazy('login'))

    def test_update_user_and_redirect_after_logging(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.post(
            reverse_lazy('update_user', kwargs={'pk': user.id}),
            TEST_USER,
        )
        self.assertRedirects(response, reverse_lazy('users_index'))
        user = User.objects.get(pk=user.id)
        self.assertEqual(user.username, TEST_USER.get('username'))
        self.assertEqual(user.first_name, TEST_USER.get('first_name'))
        self.assertEqual(user.last_name, TEST_USER.get('last_name'))

    def test_user_can_update_only_himself(self):
        self.assertEqual(User.objects.all().count(), 1)
        user_1 = User.objects.all().first()
        other_user = User.objects.create_user(
            username='Test',
            password='qwerty'
        )
        self.assertEqual(User.objects.all().count(), 2)
        self.client.force_login(user=other_user)
        response = self.client.post(
            reverse_lazy('update_user', kwargs={'pk': user_1.id}),
            TEST_USER
        )
        self.assertRedirects(response, reverse_lazy('users_index'))
        user = User.objects.get(pk=user_1.id)
        self.assertEqual(user, user_1)
