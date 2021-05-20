from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# func to be called after to Save User Signal is sent:
# only dispatch whrn we are Creating a new User,
# not every time we Save to DB the same USer


def post_user_created_signal(sender, instance, created, **kwargs):
    print("instance", instance)
    if created:
        UserProfile.objects.create(user=instance)


# SIGNAL 2 arg: (name of the func to be called , the Model that send the event)
post_save.connect(post_user_created_signal, sender=User)


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name} - {self.first_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
