from django.db import models
from django.db.models import CASCADE


class Message(models.Model):
    sender = models.ForeignKey(
        'user.User', on_delete=CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(
        'user.User', on_delete=CASCADE, related_name='received_messages')
    message = models.TextField()
    subject = models.CharField(max_length=256)
    creation_date = models.DateTimeField(
        verbose_name='Creation date', auto_now_add=True, editable=False)
    unread = models.BooleanField('Unread', default=True)

    def read(self):
        """Read the message"""
        if self.unread:
            self.unread = False
            self.save()
