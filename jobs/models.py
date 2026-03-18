from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)   # ✅ ADD THIS
    location = models.CharField(max_length=100)
    salary = models.IntegerField()
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)