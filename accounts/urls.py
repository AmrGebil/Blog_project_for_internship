from django.urls import path
from .views import register_Account

app_name = "users"

urlpatterns = [
path('register/', register_Account, name='register'),
]