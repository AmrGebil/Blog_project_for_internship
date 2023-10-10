from django.core.management.base import BaseCommand
from blog.models import Tag,Post,Comment,LikeDislike,Bookmark
from django.contrib.auth import get_user_model
from faker import Faker
import random
# this class to create Tags

# class Command(BaseCommand):
#     help = 'Generate fake tags'
#
#     def handle(self, *args, **kwargs):
#         fake = Faker()
#
#         for _ in range(10):
#             name = fake.word()
#             tag = Tag(name=name)
#             tag.save()
#
#             self.stdout.write(self.style.SUCCESS(f'Created tag: {name}'))
#
#         self.stdout.write(self.style.SUCCESS('Fake tags created successfully.'))

# this class to create users
#
# User = get_user_model()
# class Command(BaseCommand):
#     help = 'Generate fake users and set their passwords to "amr12345"'
#
#     def handle(self, *args, **kwargs):
#         fake = Faker()
#         users = []
#
#         for _ in range(10):
#             username = fake.user_name()
#             email = fake.email()
#             password = "amr12345"
#             user = User.objects.create_user(username=username, email=email, password=password)
#             users.append(user.id)
#
#             self.stdout.write(self.style.SUCCESS(f'Created user: {username} ({email})'))
#
#         self.stdout.write(self.style.SUCCESS('Fake users created successfully.'))

# this class to create posts

# User = get_user_model()
#
# class Command(BaseCommand):
#     help = 'Generate fake posts'
#
#     def handle(self, *args, **kwargs):
#         fake = Faker()
#         users = User.objects.all()
#         tags = Tag.objects.all()
#
#         for _ in range(10):
#             title = fake.sentence()
#             author = random.choice(users)
#             body = fake.paragraph()
#             post = Post.objects.create(title=title, author=author, body=body)
#             post.Tags.set(random.sample(list(tags), random.randint(0, len(tags))))
#
#             self.stdout.write(self.style.SUCCESS(f'Created post: {title} by {author.username}'))
#
#         self.stdout.write(self.style.SUCCESS('Fake posts created successfully.'))

# this class to create coments

# User = get_user_model()
#
# class Command(BaseCommand):
#     help = 'Generate fake comments'
#
#     def handle(self, *args, **kwargs):
#         fake = Faker()
#         users = User.objects.all()
#         posts = Post.objects.all()
#
#         for _ in range(20):
#             post = random.choice(posts)
#             author = random.choice(users)
#             body = fake.paragraph()
#
#             # Create a new Comment instance and save it
#             comment = Comment.objects.create(post=post, author=author, body=body)
#
#             self.stdout.write(self.style.SUCCESS(f'Created comment: {comment.body[:20]} by {author.username}'))
#
#         self.stdout.write(self.style.SUCCESS('Fake comments created successfully.'))


# this class to create LikeDislike

# User = get_user_model()
#
# class Command(BaseCommand):
#     help = 'Generate fake likes/dislikes'
#
#     def handle(self, *args, **kwargs):
#         fake = Faker()
#         users = User.objects.all()
#         posts = Post.objects.all()
#
#         for _ in range(30):
#             post = random.choice(posts)
#             author = random.choice(users)
#             is_like = random.choice([True, False])
#
#             like_dislike = LikeDislike.objects.create(author=author, post=post, is_like=is_like)
#
#             action = "liked" if is_like else "disliked"
#             self.stdout.write(self.style.SUCCESS(f'{author.username} {action} {post.title}'))
#
#         self.stdout.write(self.style.SUCCESS('Fake likes/dislikes created successfully.'))



# this class to create Bookmark
#
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

