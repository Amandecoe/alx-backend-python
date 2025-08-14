from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser): 
  #inherits all the contents from django's built in 
  # abstract user which contains username, profile
  # etc 
  profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
  #Image field is a field in python which allows uploading images
  #Upload_to = Saves images to MEDIA_ROOT/profile_pics/
  #null = true means profile_picture can be null or blank too 
  online_status = models.BooleanField(default=False)
  #checks if a user is online or not
  #Boolean field is used to check true or false conditions
  #default = false means user is offline initially
  class meta: 
    #meta is django's built in class where you add additional info 
    #excluding the one's you defined in the user class
    verbose_name = 'User'
    #shows as 'User' instead of the one you gave the class you defined
    verbose_name_plural = 'Users'
    #plural name of the user
    db_table = 'User'
    #stores in a table named 'Users'
    ordering = ['date_joined']
    #orders data by registration date
    def __str__(self):
      #controls how your model instances appear
      #as strings throughout django
      #controls amin interface display
      return self.username
    
class conversation():
      participants = models.ManyToManyField('User', related_name= 'conversations')

    
