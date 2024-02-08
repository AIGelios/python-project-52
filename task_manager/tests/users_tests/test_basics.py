from task_manager import TestCase, reverse_lazy


class NavbarTest(TestCase):

    def test_navbar_contains_correct_links(self):
        correct_navbar_links = ('users_index', 'login', 'create_user')
        response = self.client.get(reverse_lazy('homepage'))
        for link in correct_navbar_links:
            url_path = reverse_lazy(link)
            self.assertContains(response, url_path)

    def test_userlist_without_login(self):
        response = self.client.get(reverse_lazy('users_index'))
        self.assertEqual(response.status_code, 200)
