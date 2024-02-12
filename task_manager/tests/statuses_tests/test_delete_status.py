from task_manager.apps.users.models import User
from task_manager.apps.statuses.models import Status
from task_manager.apps.tools import TestCase, reverse_lazy


def delete_status_url(status_id):
    return reverse_lazy('delete_status', kwargs={'pk': status_id})


class DeleteStatusTest(TestCase):
    fixtures = ['statuses_database.json']

    def test_delete_status_page_without_login(self):
        response = self.client.get(delete_status_url(1))
        self.assertEqual(response.status_code, 302)

    def test_delete_status_page_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        response = self.client.get(delete_status_url(1))
        self.assertEqual(response.status_code, 200)

    def test_delete_status_without_login(self):
        self.assertEqual(Status.objects.all().count(), 1)
        self.client.post(delete_status_url(1))
        self.assertEqual(Status.objects.all().count(), 1)

    def test_delete_status_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        self.assertEqual(Status.objects.all().count(), 1)
        self.client.post(delete_status_url(1))
        self.assertEqual(Status.objects.all().count(), 0)
