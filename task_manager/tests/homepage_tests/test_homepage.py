from task_manager.tools import SimpleTestCase, reverse_lazy


class HomepageTest(SimpleTestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_navbar_contains_correct_links(self):
        correct_navbar_links = ('users_index', 'login', 'create_user')
        response = self.client.get(reverse_lazy('homepage'))
        for link in correct_navbar_links:
            url_path = reverse_lazy(link)
            self.assertContains(response, url_path)
