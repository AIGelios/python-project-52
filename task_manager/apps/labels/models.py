from django.db.models import Model, CharField, DateTimeField


class Label(Model):
    name = CharField(max_length=255, unique=True, blank=False)
    created_at = DateTimeField(auto_now_add=True)
