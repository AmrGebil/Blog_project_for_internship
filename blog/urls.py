from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns for your app
    path('tags/', views.TagListView.as_view(), name='tag-list'),
]