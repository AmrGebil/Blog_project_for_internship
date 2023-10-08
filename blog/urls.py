from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, CommentViewSet, PostViewSet,LikeDislikeViewSet,BookmarkListView,BookmarkCreateView,BookmarkDeleteView



router = DefaultRouter()
router.register(r"Tags", CategoryViewSet)
router.register(r"^(?P<post_id>\d+)/comment", CommentViewSet)
router.register(r"^(?P<post_id>\d+)/like_dislike", LikeDislikeViewSet)
router.register(r"", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('bookmarks/create/', BookmarkCreateView.as_view(), name='bookmark-create'),
    path('bookmarks/<int:post_id>/', BookmarkDeleteView.as_view(), name='bookmark-delete'),  # Include post_id in URL
    path('bookmarks/list/', BookmarkListView.as_view(), name='bookmark-list'),

]