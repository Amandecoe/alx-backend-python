from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import sender, Notification

@receiver(post_save, sender = sender, dispatch_uid = 'Send a Notification when User sends a Message')
def send_notification(sender, instance, created, **kwargs):
  """Send a notification when a message instance is created"""
  if created:
    Notification.objects.create(
            user = instance.sender,   
            message=f"Your post '{instance.content}' was created successfully!"
        )
