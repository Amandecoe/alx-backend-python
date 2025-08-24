from django.shortcuts import render,  get_object_or_404
from .models import Message

# Create your views here.
def message_history_view(request, message_id):
  message = get_object_or_404(Message, id = message_id)
  #gets the specific message by its id, if it doesn't exist it returns 404 page
  history = message.history.order_by('_edited_at')
  #fetches all associated history of that message
  context = {
    'message': message,
    'history' : history,
  }
  #the specific message and its history are passed to this list context
  return render(request, context)
  #renders the template with context