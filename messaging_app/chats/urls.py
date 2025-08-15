from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet

router = DefaultRouter()
#Automatically creates a RESTful URLs for the viewset
router.register(r'conversations', ConversationViewSet)
#Registers the conversationview at /conversations/
urlpatterns = router.urls
#connects all these URLS to Django's routing system