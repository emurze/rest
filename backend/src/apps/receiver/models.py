from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import ForeignKey
from taggit.managers import TaggableManager

User = get_user_model()


class Women(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    tags = TaggableManager()
    user = ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
