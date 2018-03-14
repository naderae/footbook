from django.conf import settings
from django.urls import reverse
from django.db import models
# slugify allows us to remove all characters that arent number, letters, hyphen, or underscore
from django.utils.text import slugify
from accounts.models import User
# this allows us to do link embedding in text!
import misaka
# this returns the user model that is active in this project
from django.contrib.auth import get_user_model
# now, we can call things off the users session with User. this is the user using the app, not neccessarily a logged in user.
User = get_user_model()


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    members = models.ManyToManyField(User,through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # we must format the slug so that we can use it in our url
        self.slug = slugify(self.name)
        # ensure we save everything
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']

class GroupMember(models.Model):

        group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)

        user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)

        def __str__(self):
            return self.user.username

        class Meta:
            # when taken together, they must be unique
            # every group is uniquely linked to a user
            unique_together = ('group', 'user')
