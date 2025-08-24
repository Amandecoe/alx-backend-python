from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model
# Create your models here.
class sender(models.Model):
  sender_id = models.PositiveIntegerField(primary_key=True)
  sender_name = models.CharField(max_length=100)
  email = models.EmailField(unique= True, null= False, blank= False)

class receiver(models.Model):
  receiver_id = models.PositiveIntegerField(primary_key = True)
  receiver_name = models.CharField(max_length=100)
  email = models.EmailField(unique = True, null = False, blank = False)
  senders_id = models.ForeignKey(sender, on_delete = models.CASCADE)
  
class content(models.Model):
  content_id = models.PositiveIntegerField(primary_key = True)
  content_body = models.TextField(max_length = 250, null = False)
  sent_at = models.DateTimeField(auto_now_add = True)

class timestamp(models.Model):
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

class Message(models.Model):
 message_id = models.PositiveIntegerField(primary_key = True)
 message_body = models.CharField(max_length = 250, null = False)
 edited = models.TextField(max_length = 100, blank = True, null = True)
 is_edited = models.BooleanField(default = False)

class Notification(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
  Sender = models.ForeignKey(sender, on_delete=models.CASCADE)
  message = models.CharField(max_length=255)
  is_read = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
 
class MessageHistory(models.Model):
  message = models.ForeignKey(Message, on_delete = models.CASCADE, related_name = "history")
  content = models.TextField()
  edited_at = models.DateTimeField()
  edited_by = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)