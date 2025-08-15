from django.shortcuts import render
from rest_framework import viewsets
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
# Create your views here.
class ConversationViewSet(viewsets.ModelViewSet):
  queryset = Conversation.object.all()
  #where query is run from 
  serializer_class = ConversationSerializer
  #serializer we use when returning this data
  
