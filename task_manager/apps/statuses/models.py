from django.db.models import Model, CharField, DateTimeField


class Status(Model):
    name = CharField(max_length=255, unique=True, blank=False)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
