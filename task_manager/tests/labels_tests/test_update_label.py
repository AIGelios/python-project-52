from task_manager.apps.users.models import User
from task_manager.apps.labels.models import Label
from task_manager.tools import TestCase, reverse_lazy


def update_label_url(label_id):
    return reverse_lazy('update_label', kwargs={'pk': label_id})


class UpdateLabelTest(TestCase):
    fixtures = ['labels_database.json']

    def test_update_label_page_without_login(self):
        response = self.client.get(update_label_url(1))
        self.assertEqual(response.status_code, 302)

    def test_update_label_page_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        response = self.client.get(update_label_url(1))
        self.assertEqual(response.status_code, 200)

    def test_update_label_without_login(self):
        self.assertEqual(Label.objects.all().count(), 2)
        self.client.post(update_label_url(1), {'name': 'Test label 3'})
        labels = Label.objects.all()
        self.assertEqual(labels.count(), 2)
        self.assertEqual(labels.first().pk, 1)
        self.assertEqual(labels.first().name, 'Test label 1')

    def test_update_label_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        self.assertEqual(Label.objects.all().count(), 2)
        self.client.post(update_label_url(1), {'name': 'Test label 3'})
        labels = Label.objects.all()
        self.assertEqual(labels.count(), 2)
        self.assertEqual(labels.first().pk, 1)
        self.assertEqual(labels.first().name, 'Test label 3')
