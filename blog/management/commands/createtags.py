from django.core.management.base import BaseCommand
from blog.models import Tag
from faker import Faker



class Command(BaseCommand):
    help = 'Generate fake tags'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):
            name = fake.word()
            tag = Tag(name=name)
            tag.save()

            self.stdout.write(self.style.SUCCESS(f'Created tag: {name}'))

        self.stdout.write(self.style.SUCCESS('Fake tags created successfully.'))