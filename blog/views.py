from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tag, Comment, Post,LikeDislike,Bookmark
from .serializers import TagReadSerializer, CommentReadSerializer,CommentWriteSerializer, PostReadSerializer, PostWriteSerializer,LikeDislikeWriteSerializer,LikeDislikeReadSerializer,BookmarkSerializer,BookmarkCreateSerializer
from .permissions import IsAuthorOrReadOnly
from django.core.mail import send_mail
from django_rq import enqueue
from .jobs import send_email_job





class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List and Retrieve post categories
    """
    queryset = Tag.objects.all()
    serializer_class = TagReadSerializer
    permission_classes = (permissions.AllowAny,)

class PostViewSet(viewsets.ModelViewSet):
    """
    CRUD posts
    """
    queryset = Post.objects.filter(is_approval=True)
    def get_serializer_class(self):
        if self.action in ( "update", "partial_update", "destroy"):
            return PostWriteSerializer

        return PostReadSerializer


    def get_permissions(self):
        if self.action in ("create",):
            self.permission_classes = (permissions.IsAuthenticated,)
        elif self.action in ("update", "partial_update", "destroy"):
            self.permission_classes = (IsAuthorOrReadOnly,)
        else:
            self.permission_classes = (permissions.AllowAny,)

        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = PostWriteSerializer(data=request.data , context={'request': request})

        if serializer.is_valid():
            post = serializer.save()

            enqueue(send_email_job, post.id)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    """
    CRUD comments for a particular post
    """

    queryset = Comment.objects.all()
    serializer_class = CommentReadSerializer  # Default serializer

    def get_queryset(self):
        res = super().get_queryset()
        post_id = self.kwargs.get("post_id")
        return res.filter(post__id=post_id)

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return CommentWriteSerializer
        return CommentReadSerializer

    def get_permissions(self):
        if self.action in ("create",):
            self.permission_classes = (permissions.IsAuthenticated,)
        elif self.action in ("update", "partial_update", "destroy"):
            self.permission_classes = (IsAuthorOrReadOnly,)
        else:
            self.permission_classes = (permissions.AllowAny,)

        return super().get_permissions()

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)  # You should import the Post model
        serializer.save(author=self.request.user, post=post)

# Here, we are using the normal APIView class
class LikeDislikeViewSet(viewsets.ModelViewSet):
    """
    CRUD comments for a particular post
    """

    queryset = LikeDislike.objects.all()
    serializer_class = LikeDislikeReadSerializer  # Default serializer

    def get_queryset(self):
        res = super().get_queryset()
        post_id = self.kwargs.get("post_id")
        return res.filter(post__id=post_id)

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return LikeDislikeWriteSerializer
        return LikeDislikeReadSerializer

    def get_permissions(self):
        if self.action in ("create",):
            self.permission_classes = (permissions.IsAuthenticated,)
        elif self.action in ("update", "partial_update", "destroy"):
            self.permission_classes = (IsAuthorOrReadOnly,)
        else:
            self.permission_classes = (permissions.AllowAny,)

        return super().get_permissions()

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)  # You should import the Post model
        serializer.save(post=post, user=self.request.user)




class BookmarkCreateView(APIView):
    def post(self, request, format=None):
        serializer = BookmarkCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookmarkDeleteView(generics.DestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookmarkListView(generics.ListAPIView):
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)