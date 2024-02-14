from task_manager.apps.users.models import User
from task_manager.apps.labels.models import Label
from task_manager.apps.tools import reverse_lazy, TestCase


create_label_url = reverse_lazy('create_label')


class CreateLabelTest(TestCase):
    fixtures = ['labels_database.json']

    def test_create_label_page_without_login(self):
        response = self.client.get(create_label_url)
        self.assertEqual(response.status_code, 302)

    def test_create_label_page_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        response = self.client.get(create_label_url)
        self.assertEqual(response.status_code, 200)

    def test_create_label_without_login(self):
        self.assertEqual(Label.objects.all().count(), 1)
        self.client.post(create_label_url, {'name': 'Test label 2'})
        labels = Label.objects.all()
        self.assertEqual(labels.count(), 1)
        self.assertEqual(labels.last().pk, 1)
        self.assertNotEqual(labels.last().name, 'Test label 2')

    def test_create_label_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        self.assertEqual(Label.objects.all().count(), 1)
        self.client.post(create_label_url, {'name': 'Test label 2'})
        labels = Label.objects.all()
        self.assertEqual(labels.count(), 2)
        self.assertEqual(labels.last().pk, 2)
        self.assertEqual(labels.last().name, 'Test label 2')
