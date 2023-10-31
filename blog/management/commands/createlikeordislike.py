from django.core.management.base import BaseCommand
from blog.models import Post,LikeDislike
from django.contrib.auth import get_user_model
from faker import Faker
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Generate fake likes/dislikes'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = User.objects.all()
        posts = Post.objects.all()

        for _ in range(30):
            post = random.choice(posts)
            author = random.choice(users)
            is_like = random.choice([True, False])

            like_dislike = LikeDislike.objects.create(author=author, post=post, is_like=is_like)

            action = "liked" if is_like else "disliked"
            self.stdout.write(self.style.SUCCESS(f'{author.username} {action} {post.title}'))

        self.stdout.write(self.style.SUCCESS('Fake likes/dislikes created successfully.'))
