from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet

routers = DefaultRouter()
#Automatically creates a RESTful URLs for the viewset
routers.register(r'conversations', ConversationViewSet)
#Registers the conversationview at /conversations/
# Nested router for messages under conversations
conversations_router = routers.NestedDefaultRouter(routers, r'conversations', lookup='conversation')
#generates RESTful URLs for your viewsets, which you can define hierarchically
conversations_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [path (' ', include(routers.urls))] 
#connects all these URLS to Django's routing system