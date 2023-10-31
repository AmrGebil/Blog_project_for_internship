from django.core.management.base import BaseCommand
from blog.models import Post,Comment
from django.contrib.auth import get_user_model
from faker import Faker
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Generate fake comments'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = User.objects.all()
        posts = Post.objects.all()

        for _ in range(20):
            post = random.choice(posts)
            author = random.choice(users)
            body = fake.paragraph()

            # Create a new Comment instance and save it
            comment = Comment.objects.create(post=post, author=author, body=body)

            self.stdout.write(self.style.SUCCESS(f'Created comment: {comment.body[:20]} by {author.username}'))

        self.stdout.write(self.style.SUCCESS('Fake comments created successfully.'))

