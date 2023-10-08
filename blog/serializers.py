from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Tag, Comment, Post,LikeDislike,Bookmark

class TagReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"







class CommentReadSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"



class CommentWriteSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = serializers.HiddenField(default=None)

    class Meta:
        model = Comment
        fields = "__all__"






class LikeDislikeReadSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = LikeDislike
        fields = "__all__"


class LikeDislikeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeDislike
        fields = '__all__'
        read_only_fields = ['author', 'post']  # Make these fields read-only

    def create(self, validated_data):
        user = self.context['request'].user
        post_id = self.context['view'].kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)

        # Check if the user has already liked or disliked the post
        like_exists = LikeDislike.objects.filter(post=post, author=user).exists()

        if not like_exists:
            like_dislike = LikeDislike.objects.create(
                author=user,
                post=post,
                is_like=validated_data.get('is_like')
            )
            return like_dislike
        else:
            # Handle the case where the user has already liked/disliked
            # You can raise an exception, return an error response, or handle it as needed
            # For example:
            raise serializers.ValidationError("You have already liked/disliked this post.")
class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id', 'user', 'post', 'created_at')

class BookmarkCreateSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()

    def create(self, validated_data):
        user = self.context['request'].user
        post_id = validated_data['post_id']
        bookmark = Bookmark.objects.create(user=user, post_id=post_id)
        return bookmark



class PostReadSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)
    Tags = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    user_opinion = serializers.SerializerMethodField()
    comments = CommentReadSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

    def get_Tags(self, obj):
        categories = list(
            cat.name for cat in obj.Tags.get_queryset().only("name")
        )
        return categories


    def get_likes_count(self, obj):
        return LikeDislike.objects.filter(post=obj, is_like=True).count()

    def get_dislikes_count(self, obj):
        return LikeDislike.objects.filter(post=obj, is_like=False).count()

    def get_user_opinion(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            try:
                like_dislike = LikeDislike.objects.get(post=obj, author=user)
                return 'like' if like_dislike.is_like else 'dislike'

            except Exception as e:
                return None
        return None


class PostWriteSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = "__all__"


