from django.core.management.base import BaseCommand
from blog.models import Tag,Post
from django.contrib.auth import get_user_model
from faker import Faker
import random



User = get_user_model()

class Command(BaseCommand):
    help = 'Generate fake posts'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = User.objects.all()
        tags = Tag.objects.all()

        for _ in range(10):
            title = fake.sentence()
            author = random.choice(users)
            body = fake.paragraph()
            post = Post.objects.create(title=title, author=author, body=body)
            post.Tags.set(random.sample(list(tags), random.randint(0, len(tags))))

            self.stdout.write(self.style.SUCCESS(f'Created post: {title} by {author.username}'))

        self.stdout.write(self.style.SUCCESS('Fake posts created successfully.'))
