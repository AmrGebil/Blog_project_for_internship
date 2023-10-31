from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker



User = get_user_model()
class Command(BaseCommand):
    help = 'Generate fake users and set their passwords to "amr12345"'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = []

        for _ in range(10):
            username = fake.user_name()
            email = fake.email()
            password = "amr12345"
            user = User.objects.create_user(username=username, email=email, password=password)
            users.append(user.id)

            self.stdout.write(self.style.SUCCESS(f'Created user: {username} ({email})'))

        self.stdout.write(self.style.SUCCESS('Fake users created successfully.'))
