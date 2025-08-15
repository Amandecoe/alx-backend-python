from rest_framework import serializers
from .models import User, Message, Conversation

#converts models into JSON format

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = (
      'user_id',
      'first_name',
      'last_name',
      'email',
      'phone_number',
      'password_hash',
      'role'
    )
    
class MessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Message
    fields = (
      'message_id',
      'sender_id',
      'message_body',
      'sent_at',
    )

class ConversationSerializer(serializers.ModelSerializer):
  Message = serializers.CharField(read_only=True)
  class Meta:
    model = Conversation
    fields = (
      'conversation_id'
      'participants_id'
      'created_at'
    )