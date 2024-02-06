from django.contrib.auth.models import User


User.full_name = property(lambda self: self.get_full_name())
