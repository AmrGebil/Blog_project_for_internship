from django.urls import path
from .views import register_Account,account_login,account_logout

app_name = "users"

urlpatterns = [
path('register/', register_Account, name='register'),
    path('login/', account_login, name='login'),
   path('logout/', account_logout, name='logout'),
]