from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class review(models.Model):
    instructor = models.CharField(max_length=100)
    ratings = models.IntegerField()
    comments = models.TextField()
    course = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.instructor

    def get_absolute_url(self):
            return reverse('review-detail', kwargs={'pk': self.pk})







