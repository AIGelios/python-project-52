from task_manager.apps.tools import TestCase, reverse_lazy
from task_manager.apps.users.models import User


statuses_url = reverse_lazy('statuses_index')


class StatusesIndexTest(TestCase):
    fixtures = ['statuses_database.json']

    def test_statuses_index_without_login(self):
        response = self.client.get(statuses_url)
        self.assertEqual(response.status_code, 302)

    def test_statuses_index_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        response = self.client.get(statuses_url)
        self.assertEqual(response.status_code, 200)
