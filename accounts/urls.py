from django.urls import path
from .views import register_Account,account_login,account_logout,UserAPIView,UserProfileAPIView,UserAvatarAPIView

app_name = "users"

urlpatterns = [
path('register/', register_Account, name='register'),
    path('login/', account_login, name='login'),
   path('logout/', account_logout, name='logout'),
   path("", UserAPIView.as_view(), name="user-info"),
    path("profile/", UserProfileAPIView.as_view(), name="user-profile"),
    path("profile/avatar/", UserAvatarAPIView.as_view(), name="user-avatar"),
]