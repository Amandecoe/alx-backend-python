from django.conf import Settings
from django.core.exceptions import PermissionDenied
from datetime import datetime
import logging
import time
from collections import deque
from django.http import JsonResponse
class RequestLoggingMiddleware:
  def __init__(self, get_response): #is the function that accepts the response everytime a request is given
      self.get_response = get_response
  
  def __call__(self, request):
      user = request.user if request.user.is_authenticated else "Anonymous"
      with open ("requests.log", "a") as f:
        f.write(f"{datetime.now()} - User: {user} - Path: {request.path}\n")

      response = self.get_response(request)
      return response  


class RestrictAccessByTimeMiddleware:
   def __init__(self, get_response):
      self.get_response = get_response
   def __call__(self,request):
      current_time = datetime.now().time()
      if (18,0)< current_time <(21,0) :
       raise PermissionDenied 
         
#class to limit users to send only 5 messages per 60 seconds
class OffensiveLanguageMiddleware:
  def __init__(self, get_response):
     self.get_response =  get_response
     self.request_log = {}
     self.time_window = 60
     self.max_requests = 5
  def __call__(self,request):
     client_ip = self.get.client_ip(request) #gets the clients Ip and stores it
     now = time.time()

     if client_ip not in self.request_log:  #checks if the client's ip is in the logged ip's in our request.log file
        self.request_log[client_ip] = deque() #then it gives a client_ip an empty bucket to store the timestamp of that request

     request_times = self.request_log[client_ip] #stores the amount of times a user have requested using the client's ip from the request_log 

     while request_times and now - request_times[0] > self.time_window:
            request_times.popleft()
      # deletes the older timestamp to add a new one into the deque
     if len(request_times) > self.max_requests:  #checks the number of requests and if it passes the max requests allowed it puts out an error message
        return JsonResponse(
           {"Error":"Limit Reached Try Again Later"},
           status = 429
        )
     #logs the request if it passes the above if statement
     self.log_request(request)

        # adds the current request's timestamp since now is the time right when the request is doneS
     request_times.append(now)

     return self.get_response(request)

     
     