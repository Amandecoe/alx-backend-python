from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsParticipantOfConversation(BasePermission):
  def has_permission(self, request, view):
    return bool(request.user and request.user.is_authenticated)
  def has_object_permission(self, request, view, obj):
        # obj will be a Message instance
        conversation = obj.conversation
        return request.user in conversation.participants.all()
