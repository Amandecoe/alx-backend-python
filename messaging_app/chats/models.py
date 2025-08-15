from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser): 
  profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
  online_status = models.BooleanField(default=False)
  user_id = models.CharField(max_length=30, primary_key=True )
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(max_length=50, unique=True, null=False)
  password_hash = models.CharField(max_length = 30)
  phone_number = models.CharField(max_length=30)
  class Role(models.TextChoices):  # This is not a separate table — just an enum definition
        GUEST = 'guest', 'Guest'
        HOST = 'host', 'Host'
        ADMIN = 'admin', 'Admin'
  role = models.CharField(max_length=30, choices = Role.choices, default = Role.GUEST)
created_at = models.DateTimeField(max_length=30, auto_now_add=True)
#django will automatically set this field to the current timestamp when 
#the object is created and never change it afterward

  
    
