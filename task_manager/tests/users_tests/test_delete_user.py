from task_manager.apps.tools import TransactionTestCase, reverse_lazy
from task_manager.apps.users.models import User


class DeleteUserTest(TransactionTestCase):
    fixtures = ['users_database.json']

    def test_only_logged_user_can_delete(self):
        response = self.client.post(
            reverse_lazy('delete_user', kwargs={'pk': 1})
        )
        users = User.objects.all()
        self.assertEqual(users.count(), 1)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_user_can_delete_only_himself(self):
        user = User.objects.all().first()
        other_user = User.objects.create_user(
            username='Test',
            password='qwerty'
        )
        self.client.force_login(user=other_user)
        response = self.client.post(
            reverse_lazy('delete_user', kwargs={'pk': user.id})
        )
        users = User.objects.all()
        self.assertEqual(users.count(), 2)
        self.assertIn(user, users)
        self.assertRedirects(response, reverse_lazy('users_index'))
        response = self.client.post(
            reverse_lazy('delete_user', kwargs={'pk': other_user.id})
        )
        users = User.objects.all()
        self.assertEqual(users.count(), 1)
        self.assertIn(user, users)
        self.assertNotIn(other_user, users)
