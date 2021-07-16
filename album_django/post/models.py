from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='created_posts', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
