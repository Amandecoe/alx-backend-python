from django.shortcuts import render
from rest_framework import generics
from .models import Conversation, Message
# Create your views here.
class ConversationViewSet(generics.ListCreateAPIView):
