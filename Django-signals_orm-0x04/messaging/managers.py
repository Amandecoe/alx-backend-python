from .models import Message
from django.shortcuts import render

class UnreadMessagesManager:
  def unread_for_user(request):
   sender=request.user
   unread_messages=Message.objects.filter.only(unread = False)
  
   if sender == unread_messages:
    reply = {
      'unread_messages' : unread_messages
    }

   return render (reply) 