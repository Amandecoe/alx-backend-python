from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
# Create your views here.
class ConversationViewSet(viewsets.ModelViewSet):
  queryset = Conversation.object.all()
  #where query is run from 
  serializer_class = ConversationSerializer
  #serializer we use when returning this data
  def send_message(self, request, pk=None):
    conversation = self.get_object() #fetches conversation using the URL ID
    message_body = request.data.get('message_body') #reads the message from the request

    message = Message.objects.create( #saves a new message linked to the conversation and sender
      conversation = conversation,
      message_body = message_body
    )
    return Response(MessageSerializer(message).data, status=201) #returns the message as JSON with HTTP status 201
class MessageViewSet(viewsets.ModelViewSet):
  queryset = Message.object.all()
  serializer_class = MessageSerializer
