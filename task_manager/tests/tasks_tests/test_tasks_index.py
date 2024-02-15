from task_manager.tools import (
    TestCase, TransactionTestCase, reverse_lazy,
)
from task_manager.apps.users.models import User


tasks_index_url = reverse_lazy('tasks_index')


class TasksIndexTest(TestCase):
    fixtures = ['tasks_database.json']

    def test_tasks_index_without_login(self):
        response = self.client.get(tasks_index_url)
        self.assertEqual(response.status_code, 302)

    def test_statuses_index_with_login(self):
        self.client.force_login(user=User.objects.get(pk=1))
        response = self.client.get(tasks_index_url)
        self.assertEqual(response.status_code, 200)


class FiltersTest(TransactionTestCase):
    fixtures = ['tasks_database_2.json']

    def test_tasks_index_without_filters(self):
        self.client.force_login(user=User.objects.get(pk=1))
        response = self.client.get(tasks_index_url)
        tasks_on_page = response.context['object_list']
        self.assertEqual(tasks_on_page.count(), 4)

    def test_tasks_index_with_status_filter(self):
        self.client.force_login(user=User.objects.get(pk=1))

        response = self.client.get(tasks_index_url, {'status': 1})
        tasks = response.context['object_list']
        self.assertEqual(tasks.count(), 3)
        self.assertEqual({x.status_id for x in tasks}, {1})

        response = self.client.get(tasks_index_url, {'status': 2})
        tasks = response.context['object_list']
        self.assertEqual(tasks.count(), 1)
        self.assertEqual({x.status_id for x in tasks}, {2})

    def test_tasks_index_with_executor_filter(self):
        self.client.force_login(user=User.objects.get(pk=1))

        response = self.client.get(tasks_index_url, {'executor': 1})
        tasks = response.context['object_list']
        self.assertEqual(tasks.count(), 2)
        self.assertEqual({x.executor_id for x in tasks}, {1})

        response = self.client.get(tasks_index_url, {'executor': 2})
        tasks = response.context['object_list']
        self.assertEqual(tasks.count(), 2)
        self.assertEqual({x.executor_id for x in tasks}, {2})

    def test_tasks_index_with_label_filter(self):
        self.client.force_login(user=User.objects.get(pk=1))

        response = self.client.get(tasks_index_url, {'labels': 1})
        tasks = response.context['object_list']
        self.assertEqual(tasks.count(), 3)

        response = self.client.get(tasks_index_url, {'labels': 2})
        tasks = response.context['object_list']
        self.assertEqual(tasks.count(), 2)

    def test_tasks_index_only_owner_tasks(self):
        self.client.force_login(user=User.objects.get(pk=1))
        response = self.client.get(tasks_index_url, {'own_tasks': 'on'})
        tasks = response.context['object_list']
        self.assertEqual(tasks.count(), 1)

        self.client.force_login(user=User.objects.get(pk=2))
        response = self.client.get(tasks_index_url, {'own_tasks': 'on'})
        tasks = response.context['object_list']
        self.assertEqual(tasks.count(), 3)
