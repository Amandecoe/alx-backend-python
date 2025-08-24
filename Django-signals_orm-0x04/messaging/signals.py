from django.dispatch import receiver
from django.db.models import post_save
from .models import sender

@receiver(post_save, sender = sender, dispatch_uid = 'Send a Notification when User sends a Message')
def send_notification(sender, instance, created, **kwargs):
  """Send a notification when a message instance is created"""
  if created:
    print("New Message")
