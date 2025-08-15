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
  def validate_first_name(self, value):
    if value <=0:
       raise serializers.ValidationError(
         "No first name"
      )
    return value
    
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
  last_message = serializers.SerializerMethodField()
  #is a computed field which is not stored in the database
  #this calls a function named get_last_message when serializing a conversation
  class Meta:
    model = Conversation
    fields = (
      'conversation_id',
      'participants_id',
      'created_at',
    )
  def get_last_message(self, obj): #obj is the conversation instance being serialized
        last_msg = obj.messages.order_by('-sent_at').first()  # gets all related messages ordered by sent time
        if last_msg:
            return MessageSerializer(last_msg).data #serializes the message instance into JSON, .data gives the dictionary representation
        return None  
