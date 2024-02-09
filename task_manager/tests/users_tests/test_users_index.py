from task_manager import TestCase, reverse_lazy
from task_manager.users.models import User


class UsersIndexTest(TestCase):
    fixtures = ['users_database.json']

    def test_users_index_without_login(self):
        response = self.client.get(reverse_lazy('users_index'))
        self.assertEqual(response.status_code, 200)

    def test_users_index_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        self.test_users_index_without_login()
