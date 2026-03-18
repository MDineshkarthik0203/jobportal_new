from django.db import models

from jobs.models import Job
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL
class Application(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100,default='NOT NULL')
    resume=models.FileField(upload_to='resumes/',default='NOT NULL')
    status=models.CharField(max_length=20, default='applied')
    def __str__(self):
        return f"{self.full_name} - {self.job.title}"
