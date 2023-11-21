from django.core.mail import send_mail
from django_rq import job
from .models import Post

@job(timeout=300)
def send_email_job(post):

    send_mail(
        subject='New Post Created',
        message=f'A new post with the title "{post.title}" has been created, you can approve or reject it.',
        from_email='blogproject@example.com',
        recipient_list=['amrgebil@example.com', 'mohammed@gmail.com'],
        fail_silently=False,
    )

