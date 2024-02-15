from task_manager.apps.users.models import User
from task_manager.apps.labels.models import Label
from task_manager.tools import TestCase, reverse_lazy


def get_delete_label_url(label_id):
    return reverse_lazy('delete_label', kwargs={'pk': label_id})


class DeleteLabelTest(TestCase):
    fixtures = ['labels_database.json']

    def test_delete_label_page_without_login(self):
        response = self.client.get(get_delete_label_url(1))
        self.assertEqual(response.status_code, 302)

    def test_delete_label_page_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        response = self.client.get(get_delete_label_url(1))
        self.assertEqual(response.status_code, 200)

    def test_delete_label_without_login(self):
        self.assertEqual(Label.objects.all().count(), 2)
        self.client.post(get_delete_label_url(1))
        self.assertEqual(Label.objects.all().count(), 2)

    def test_delete_free_label_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        self.assertEqual(Label.objects.all().count(), 2)
        self.client.post(get_delete_label_url(1))
        self.assertEqual(Label.objects.all().count(), 1)

    def test_delete_not_free_label_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        self.assertEqual(Label.objects.all().count(), 2)
        self.client.post(get_delete_label_url(2))
        self.assertEqual(Label.objects.all().count(), 2)
