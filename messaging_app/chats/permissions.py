from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsParticipantOfConversation:
  def has_permission(self, request, view):
    return bool(request.user and request.user.isAuthenticated)
