from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent",null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey("Category", related_name="leads", null=True, blank=True, on_delete=models.SET_NULL)
   
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    
class Category(models.Model):
    name = models.CharField(max_length=250)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.name
    
    

    
    
# this is how we create auto user in userProfile
def post_user_created_signal(sender, instance, created, **kwargs):
    print("The created User is", sender)
    print("Is user created Or not", created)
    if created:
        # here userprofile is the another models name where we want to send signals of the user
        UserProfile.objects.create(user = instance)
        # here user defines from which model we are sending the signals where here we do have User 
post_save.connect(post_user_created_signal, sender=User)        
