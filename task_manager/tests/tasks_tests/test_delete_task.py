from task_manager.apps.users.models import User
from task_manager.apps.tasks.models import Task
from task_manager.tools import reverse_lazy, TransactionTestCase


delete_task_url = reverse_lazy('delete_task', kwargs={'pk': 1})


class DeleteTaskTest(TransactionTestCase):
    fixtures = ['tasks_database.json']

    def test_delete_task_page_without_login(self):
        response = self.client.get(delete_task_url)
        self.assertEqual(response.status_code, 302)

    def test_delete_task_page_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        response = self.client.get(delete_task_url)
        self.assertEqual(response.status_code, 200)

    def test_delete_task_without_login(self):
        self.assertEqual(Task.objects.all().count(), 1)
        self.client.post(delete_task_url)
        tasks = Task.objects.all()
        self.assertEqual(tasks.count(), 1)
        task = tasks.last()
        self.assertEqual(task.pk, 1)
        self.assertEqual(task.name, 'Test task 1')
        self.assertEqual(task.author.pk, 1)
        self.assertEqual(task.status.pk, 1)
        self.assertEqual(task.executor.pk, 2)

    def test_delete_task_with_login_as_author(self):
        self.client.force_login(user=User.objects.get(pk=1))
        self.assertEqual(Task.objects.all().count(), 1)
        self.client.post(delete_task_url)
        tasks = Task.objects.all()
        self.assertFalse(tasks)
        self.assertEqual(tasks.count(), 0)

    def test_delete_task_with_login_as_other(self):
        self.client.force_login(user=User.objects.get(pk=2))
        self.test_delete_task_without_login()
