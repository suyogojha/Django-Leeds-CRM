from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    
# this is how we create auto user in userProfile
def post_user_created_signal(sender, instance, created, **kwargs):
    print("The created User is", sender)
    print("Is user created Or not", created)
    if created:
        # here userprofile is the another models name where we want to send signals of the user
        UserProfile.objects.create(user = instance)
        # here user defines from which model we are sending the signals where here we do have User 
post_save.connect(post_user_created_signal, sender=User)        
