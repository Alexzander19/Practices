from django.db import models
from django.contrib.auth.views import LoginView
# Create your models here.

# почему в практической это размещается в views? Ведь это class = модель?
class CustomLoginView(LoginView):
  template_name = 'users/login.html'