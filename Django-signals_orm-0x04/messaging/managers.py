from .models import Message
from django.shortcuts import render

class UnreadMessagesManager:
  def unread_for_user(self, user):
   return self.filter(reciever=user, unread=False)