import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class StatusOptions(models.IntegerChoices):
    CREATED = 0, "created"
    APPROVED = 1, "approved"
    REJECTED = 2, "rejected"


class Writer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    is_editor = models.BooleanField()

    def __str__(self):
        return self.name


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.IntegerField(
        default=StatusOptions.CREATED,
        choices=StatusOptions.choices
    )
    written_by = models.ForeignKey(
        Writer,
        on_delete=models.CASCADE,
        related_name="written_by"
    )
    edited_by = models.ForeignKey(
        Writer,
        on_delete=models.CASCADE,
        related_name="edited_by"
    )

    def __str__(self):
        return self.title
