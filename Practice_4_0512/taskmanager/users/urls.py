from django.urls import path
from .models import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('login/', CustomLoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(next_page='/'), name='logout')
]