from django.db import models
# from django.contrib.auth.models import User
# from celeryApp.models import CustomUser

from django.contrib.auth import get_user_model
User = get_user_model()


class Question(models.Model):
    title = models.TextField(null=False, blank=False)
    status = models.CharField(default="Inactive", max_length=10)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (("able_to_answer", "We can give the answer"),)

    def __str__(self):
        return self.title
