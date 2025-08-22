from django.conf import Settings
from django.core.exceptions import PermissionDenied
from time import datetime
import logging

class RequestLoggingMiddleware:
  def _init_(self, get_response):
   self.get_response = get_response
  
  def __call__(self, request):
    user = 'Anonymous'
    if hasattr(request, 'user') and hasattr(request.user, 'is_Authenticated'):
      if request.user.is_Authenticated:  
        user = request.user.username

    log_message = f"{datetime.now()} - User: {user} - Path: {request.path}\n"
    with open ('requests.log', 'a') as f:
      f.write(log_message)

    response = self.get_response(request)
    return response  

