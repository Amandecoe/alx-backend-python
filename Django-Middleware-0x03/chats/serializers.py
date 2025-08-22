# serializers.py
# serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

# Get User model safely
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user_id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'role'
        )
    
    def validate_first_name(self, value):
        if not value:
            raise serializers.ValidationError("First name is required")
        return value

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        # Import Message inside the class to avoid circular import
        model = None
    
    def __init__(self, *args, **kwargs):
        from .models import Message  # Import here
        self.Meta.model = Message
        super().__init__(*args, **kwargs)
    
    class Meta:
        fields = (
            'message_id',
            'sender_id',
            'message_body',
            'sent_at',
        )

class ConversationSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField()
    
    class Meta:
        # Import Conversation inside the class to avoid circular import
        model = None
    
    def __init__(self, *args, **kwargs):
        from .models import Conversation  # Import here
        self.Meta.model = Conversation
        super().__init__(*args, **kwargs)
    
    class Meta:
        fields = (
            'conversation_id',
            'participants',
            'created_at',
            'last_message'
        )
    
    def get_last_message(self, obj):
        from .models import Message  # Import here
        last_msg = Message.objects.filter(conversation=obj).order_by('-sent_at').first()
        if last_msg:
            return MessageSerializer(last_msg).data
        return None