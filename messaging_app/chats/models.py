from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
# Create your models here.
class User(AbstractUser): 
  profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
  online_status = models.BooleanField(default=False)
  user_id = models.UUIDField(max_length=30, primary_key=True, default=uuid.uuid4, db_index=True)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(max_length=50, unique=True, null=False, db_index = True)
  password_hash = models.CharField(max_length = 30)
  phone_number = models.PositiveIntegerField(unique=True)
  class Role(models.TextChoices):  # This is not a separate table — just an enum definition
        GUEST = 'guest', 'Guest'
        HOST = 'host', 'Host'
        ADMIN = 'admin', 'Admin'
  role = models.CharField(max_length=30, choices = Role.choices, default = Role.GUEST)
created_at = models.DateTimeField(max_length=30, auto_now_add=True)
#django will automatically set this field to the current timestamp when 
#the object is created and never change it afterward


class Message(models.Model):
    message_id = models.UUIDField(max_length=30, primary_key=True, default=uuid.uuid4, db_index=True)
    sender_id = models.ForeignKey(User, on_delete = models.CASCADE)
    #this references the primary key of User which is user_id
    message_body = models.CharField(max_length=30, null = False)
    sent_at = models.DateTimeField(max_length=30, auto_now_add = True)


class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, db_index = True, default = uuid.uuid4)
    participants_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    #auto_now_add = sets the timestamp once on creation






  
    
