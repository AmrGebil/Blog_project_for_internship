from django.conf import settings
from django.db import models


class Tag(models.Model):
    name = models.CharField( max_length=100)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField( max_length=250)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="posts",
        null=True,
        on_delete=models.SET_NULL,
    )
    tags = models.ManyToManyField(Tag, related_name="posts_list", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.title} by {self.author.username}"

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="post_comments",
        null=True,
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.content[:20]} by {self.author.username}"


class LikeDislike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)  # True for like, False for dislike

    def __str__(self):
        return f"{self.user.username} {'liked' if self.is_like else 'disliked'} {self.post.title}"

class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} bookmarked {self.post.title}"