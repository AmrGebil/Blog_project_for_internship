from rest_framework import serializers
from .models import Post, Comment, Tag, LikeDislike

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class LikeDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeDislike
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    likes = LikeDislikeSerializer(many=True, read_only=True)
    dislikes = LikeDislikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'