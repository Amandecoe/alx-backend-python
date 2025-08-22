from django.conf import Settings
from django.core.exceptions import PermissionDenied
from datetime import datetime
import logging

class RequestLoggingMiddleware:
  def __init__(self, get_response): #is the function that accepts the response everytime 
      self.get_response = get_response
  
  def __call__(self, request):
      user = request.user if request.user.is_authenticated else "Anonymous"
      with open ("requests.log", "a") as f:
        f.write(f"{datetime.now()} - User: {user} - Path: {request.path}\n")

      response = self.get_response(request)
      return response  


class  RestrictAccessByTimeMiddleware:
   def __init__(self, get_response):
      self.get_response = get_response
   def __call__(self,request):
      user = request.user if request.user.is_authenticated else "Anonymous"
      current_time = datetime.now().time()
      if (18,0)< current_time <(21,0) :
       raise PermissionDenied 
         
