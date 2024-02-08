from task_manager import TestCase, reverse_lazy


class UsersIndexTest(TestCase):
    def test_userlist_without_login(self):
        response = self.client.get(reverse_lazy('users_index'))
        self.assertEqual(response.status_code, 200)
