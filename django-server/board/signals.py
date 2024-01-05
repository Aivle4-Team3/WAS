from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment
from accounts.models import User, UserMessage


@receiver(post_save, sender=Comment)
def send_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        user = User.objects.get(id=post.author_id)

        message = UserMessage(user=user, sender=instance.author, message=f'{instance.author}님이 "{post}"에 댓글을 달았습니다')
        message.save()
