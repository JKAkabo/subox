import uuid

from django.contrib.auth.models import User
from django.db import models

PRIORITY_LEVELS = (
    (1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
)


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    holder = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=100)
    cost = models.DecimalField(max_digits=19, decimal_places=2)
    priority = models.PositiveIntegerField(choices=PRIORITY_LEVELS, default=1)
    time_added = models.DateTimeField(auto_now_add=True)
