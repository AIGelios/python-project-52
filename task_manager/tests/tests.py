# Homepage test
from .homepage_tests.test_homepage import HomepageTest  # noqa

# Users page and CRUD tests
from .users_tests.test_basics import UsersIndexTest  # noqa
from .users_tests.test_create_user import CreateUserTest  # noqa
from .users_tests.test_update_user import UpdateUserTest  # noqa
from .users_tests.test_delete_user import DeleteUserTest  # noqa

# Statuses page and CRUD tests
from .statuses_tests.test_basics import StatusesIndexTest  # noqa
