from django.db import models
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import AbstractUser
# Create your models here.

# почему в практической это размещается в views? Ведь это class = модель?
# class CustomLoginView(LoginView):
#   template_name = 'users/login.html'

# class User(AbstractUser):
#   firstname = models.CharField(max_length=100)
#   lastname = models.CharField(max_length=100)

#   def __str__(self):
#     return self.username