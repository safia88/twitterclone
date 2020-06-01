from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
# from django.contrib.auth.models import User

# Create your models here.
User = settings.AUTH_USER_MODEL


class TwitterUser (AbstractUser):
    phone = models.CharField(null=True, max_length=15)


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     follows = models.ManyToManyField(
#         'self', related_name='followed_by', symmetrical=False)


# """similarly it also create table automatically in database."""
# User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class FollowModel(models.Model):
    follower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 blank=True, related_name='follower')
    followed = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 blank=True, related_name='followed')

    def __str__(self):
        return 'Follower: ' + self.follower.username + ' / Followed: ' + self.followed.username
