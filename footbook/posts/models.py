from django.conf import settings
from django.urls import reverse
from django.db import models

import misaka

from groups.models import  Group

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # when you are reversing, you have to pass in the info that is required by the url as kwargs.
        return reverse(
            "posts:single",
            kwargs={
                "slug": self.group.slug,
                "pk":self.pk
            }

        )

    class Meta:
        # odering = ['-created_at']
        # a post can belong to only one combination of user and group
        # if a post belongs to a user1 and group1, and another post belongs to user1 and group2
        # a post can only be associated with unique combinations of a user and a group
        unique_together = ['user', 'group']
