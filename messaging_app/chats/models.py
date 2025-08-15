from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser): 
  profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
  online_status = models.BooleanField(default=False)
  class meta: 
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

    
