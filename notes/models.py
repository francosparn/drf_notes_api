from django.db import models
from users.models import User


class Note(models.Model):
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
