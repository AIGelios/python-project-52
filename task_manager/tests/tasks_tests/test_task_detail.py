from task_manager.apps.tools import TransactionTestCase, reverse_lazy
from task_manager.apps.users.models import User
from task_manager.apps.tasks.models import Task
from task_manager.apps.statuses.models import Status


task_details_url = reverse_lazy('task_detail', kwargs={'pk': 1})


class TaskDetailTest(TransactionTestCase):
    fixtures = ['tasks_database.json']

    def test_task_detail_page_without_login(self):
        response = self.client.get(task_details_url)
        self.assertEqual(response.status_code, 302)

    def test_task_detail_page_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        response = self.client.get(task_details_url)
        self.assertEqual(response.status_code, 200)

    def test_task_detail_with_login(self):
        author = User.objects.get(pk=1)
        self.client.force_login(user=author)
        performer = User.objects.get(pk=2)
        tasks = Task.objects.all()
        statuses = Status.objects.all()
        self.assertEqual(tasks.count(), 1)
        self.assertEqual(statuses.count(), 1)
        task = tasks.first()
        status = statuses.first()
        self.assertEqual(task.author, author)
        self.assertEqual(task.performer, performer)
        self.assertEqual(task.status, status)
