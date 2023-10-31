
from django.core.management.base import BaseCommand
from blog.models import Post,Bookmark
from django.contrib.auth import get_user_model
from faker import Faker
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Generate fake bookmarks'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = User.objects.all()
        posts = Post.objects.all()

        for _ in range(20):
            post = random.choice(posts)
            user = random.choice(users)

            bookmark = Bookmark.objects.create(user=user, post=post)

            self.stdout.write(self.style.SUCCESS(f'{user.username} bookmarked {post.title}'))

        self.stdout.write(self.style.SUCCESS('Fake bookmarks created successfully.'))

