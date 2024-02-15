from task_manager.apps.users.models import User
from task_manager.apps.tasks.models import Task
from task_manager.apps.tools import reverse_lazy, TransactionTestCase


create_task_url = reverse_lazy('create_task')


class CreateTaskTest(TransactionTestCase):
    fixtures = ['tasks_database.json']

    def test_create_task_page_without_login(self):
        response = self.client.get(create_task_url)
        self.assertEqual(response.status_code, 302)

    def test_creatre_task_page_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        response = self.client.get(create_task_url)
        self.assertEqual(response.status_code, 200)

    def test_create_task_without_login(self):
        self.assertEqual(Task.objects.all().count(), 1)
        self.client.post(
            create_task_url,
            {
                'name': 'Test task 2',
                'description': 'Make something',
                'author': 2,
                'status': 1,
                'executor': 1,
            },
        )
        tasks = Task.objects.all()
        self.assertEqual(tasks.count(), 1)
        task = tasks.last()
        self.assertEqual(task.pk, 1)
        self.assertEqual(task.name, 'Test task 1')
        self.assertEqual(task.author.pk, 1)
        self.assertEqual(task.status.pk, 1)
        self.assertEqual(task.executor.pk, 2)

    def test_create_task_with_login(self):
        self.client.force_login(user=User.objects.get(pk=2))
        self.assertEqual(Task.objects.all().count(), 1)
        self.client.post(
            create_task_url,
            {
                'name': 'Test task 2',
                'description': 'Make something',
                'author': 2,
                'status': 1,
                'executor': 1,
            },
        )
        tasks = Task.objects.all()
        self.assertEqual(tasks.count(), 2)
        task = tasks.last()
        self.assertEqual(task.pk, 2)
        self.assertEqual(task.name, 'Test task 2')
        self.assertEqual(task.author.pk, 2)
        self.assertEqual(task.status.pk, 1)
        self.assertEqual(task.executor.pk, 1)
