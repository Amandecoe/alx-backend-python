from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete
from django.utils import timezone
from django.contrib.auth.models import User
from .models import sender, Notification, MessageHistory, Message

@receiver(post_save, sender = sender, dispatch_uid = 'Send a Notification when User sends a Message')
def send_notification(sender, instance, created, **kwargs):
  """Send a notification when a message instance is created"""
  if created:
    Notification.objects.create(
            user = instance.sender,   
            message=f"Your post '{instance.content}' was created successfully!"
        )

@receiver(pre_save, sender = Message ,dispatch_uid = 'Saves older message')
def save_old_content(sender, instance, **kwargs):
  """Save the old content of the message before an edit """
  old_message = Message.objects.get(pk = instance.message_id) 
  #This variable stores the existing message from the database that has the same primary key as the one we are about to save(the edit)
  #instance is the current message object to be saved
  if old_message.content != instance.content:
    #instance refers to the specific object being saved
    MessageHistory.objects.create(
     message = instance,
     content = old_message.content,
     edited_At = timezone.now()
    )

@receiver(post_delete, sender = User, dispatch_uid = 'delete user')
def delete_user_data(sender, instance, **kwargs):
      messages = Message.objects.filter(sender = instance)
      #fetches all the messages of that sender
      for msg in messages:
         msg.delete()
         #deletes all the messages of the user
      received_messages = Message.objects.filter(receiver = instance)
      #fetches all the messages received by that user
      for msg in received_messages:
         msg.delete()
         #deletes all the received messages   
      