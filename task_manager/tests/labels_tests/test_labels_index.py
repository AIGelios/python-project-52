from task_manager.tools import TestCase, reverse_lazy
from task_manager.apps.users.models import User


labels_url = reverse_lazy('labels_index')


class LabelsIndexTest(TestCase):
    fixtures = ['labels_database.json']

    def test_labels_index_without_login(self):
        response = self.client.get(labels_url)
        self.assertEqual(response.status_code, 302)

    def test_labels_index_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        response = self.client.get(labels_url)
        self.assertEqual(response.status_code, 200)
