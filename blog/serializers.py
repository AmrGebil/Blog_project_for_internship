from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Tag, Comment, Post,LikeDislike

class TagReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class PostReadSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)
    categories = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

    def get_categories(self, obj):
        categories = list(
            cat.name for cat in obj.Tags.get_queryset().only("name")
        )
        return categories

    def get_likes(self, obj):
        likes = list(
            like.username for like in obj.likes.get_queryset().only("username")
        )
        return likes

class PostWriteSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
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

