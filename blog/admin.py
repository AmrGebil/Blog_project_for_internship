from django.contrib import admin
from .models import Post,Comment,LikeDislike,Bookmark,Tag
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(LikeDislike)
admin.site.register(Bookmark)
admin.site.register(Tag)
