from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet

routers = DefaultRouter()
#Automatically creates a RESTful URLs for the viewset
routers.register(r'conversations', ConversationViewSet)
#Registers the conversationview at /conversations/
urlpatterns = [path (' ', include(router.irls))] 
#connects all these URLS to Django's routing system