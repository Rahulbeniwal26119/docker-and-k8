from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
# Create your models here.


class CustomUser(AbstractUser):
    staff_member = models.BooleanField(default=False)
    user_info = HTMLField(null=True)

    def __unicode__(self):
        return self.username


class FeedBack(models.Model):
    RATING_CHOICES = (
        (0, 'Bad'),
        (1, 'Fine'),
        (2, 'Excellent')
    )
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True)
    message = models.TextField()
    rating = models.IntegerField(default=0, choices=RATING_CHOICES)
