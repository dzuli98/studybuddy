from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null = True) #if topic placed below in the code, wrap it in ''
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True) #auto_now takes the snapshot everytime we save
    created = models.DateTimeField(auto_now_add=True) #auto_now_add takes the snapshot the first time it is created

    class Meta:
        ordering = ['-updated', '-created'] #- reverts it

    def __str__(self):
        return self.name

class Message(models.Model): # here one to many relationship is introduced
    user = models.ForeignKey(User, on_delete=models.CASCADE) # rooms can have multiple messages, but message can belong to one user/room     
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # if room is deleted all the messages are deleted as well
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created'] #- reverts it
        
    def __str__(self):
        return self.body[0:50]