from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager import reverse_lazy, TestCase


create_status_url = reverse_lazy('create_status')


class CreateStatusTest(TestCase):
    fixtures = ['statuses_database.json']

    def test_create_status_page_without_login(self):
        response = self.client.get(create_status_url)
        self.assertEqual(response.status_code, 302)

    def test_create_status_page_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        response = self.client.get(create_status_url)
        self.assertEqual(response.status_code, 200)

    def test_create_status_without_login(self):
        self.assertEqual(Status.objects.all().count(), 1)
        self.client.post(create_status_url, {'name': 'Test status 2'})
        statuses = Status.objects.all()
        self.assertEqual(statuses.count(), 1)
        self.assertEqual(statuses.last().pk, 1)
        self.assertNotEqual(statuses.last().name, 'Test status 2')

    def test_create_status_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        self.assertEqual(Status.objects.all().count(), 1)
        self.client.post(create_status_url, {'name': 'Test status 2'})
        statuses = Status.objects.all()
        self.assertEqual(statuses.count(), 2)
        self.assertEqual(statuses.last().pk, 2)
        self.assertEqual(statuses.last().name, 'Test status 2')
