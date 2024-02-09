from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager import TestCase, reverse_lazy


def update_status_url(status_id):
    return reverse_lazy('update_status', kwargs={'pk': status_id})


class UpdateStatusTest(TestCase):
    fixtures = ['statuses_database.json']

    def test_update_status_page_without_login(self):
        response = self.client.get(update_status_url(1))
        self.assertEqual(response.status_code, 302)

    def test_update_status_page_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        response = self.client.get(update_status_url(1))
        self.assertEqual(response.status_code, 200)

    def test_update_status_page_without_login(self):
        self.assertEqual(Status.objects.all().count(), 1)
        self.client.post(update_status_url(1), {'name': 'Test status 2'})
        statuses = Status.objects.all()
        self.assertEqual(statuses.count(), 1)
        self.assertEqual(statuses.first().pk, 1)
        self.assertEqual(statuses.first().name, 'Test status 1')    
    
    def test_update_status_page_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        self.assertEqual(Status.objects.all().count(), 1)
        self.client.post(update_status_url(1), {'name': 'Test status 2'})
        statuses = Status.objects.all()
        self.assertEqual(statuses.count(), 1)
        self.assertEqual(statuses.first().pk, 1)
        self.assertEqual(statuses.first().name, 'Test status 2')
