from rest_framework.response import Response
from rest_framework import viewsets
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from rest_framework.decorators import action
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsParticipantOfConversation
from rest_framework import status
from .pagination import MessageFilter
# Create your views here.
class ConversationViewSet(viewsets.ModelViewSet):
  queryset = Conversation.objects.all()
  #where query is run from 
  serializer_class = ConversationSerializer
  #serializer we use when returning this data
  permission_classes = [IsAuthenticated, IsParticipantOfConversation]
  def send_message(self, request, pk=None):
    conversation = self.get_object() #fetches conversation using the URL ID
    message_body = request.data.get('message_body') #reads the message from the request

    message = Message.objects.create( #saves a new message linked to the conversation and sender
      conversation = conversation,
      sender=request.user,
      message_body = message_body
    )
    return Response(MessageSerializer(message).data, status=201) #returns the message as JSON with HTTP status 201
class MessageViewSet(viewsets.ModelViewSet):
  queryset = Message.objects.all()
  serializer_class = MessageSerializer
  permission_class = [IsAuthenticated]
  pagination_class = MessageFilter

  def get_queryset(self):   
   conversation_id = self.kwargs.get("conversation_id") #You store the URL patterns captured by your routers here using kwargs.get
   return Message.objects.filter(conversation_id=conversation_id, conversation_participants = self.request.user).order_by('created_at')
  #this checks if the conversation_id is the same as the one captured, and also if the user is participant of that conversation

  #checks if the user is part of the conversation
  def create(self, request, *args, **kwargs):
    conversation_id = self.kwargs.get("conversation_id")
    if not Conversation.objects.filter(conversation_id = conversation_id, conversation_participants = self.request.user).exists():
      #Checks if the conversation_id matches with the URL stored and also the participants and gives the following response
      return Response(
        {"detail: You are not a participant of this conversation"},
        status= status.HTTP_403_FORBIDDEN
      )
    

