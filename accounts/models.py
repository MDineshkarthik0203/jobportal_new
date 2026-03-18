from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES =(
        ('candidate','Candidate'),
        ('recruiter','Recruiter'),
    )
    role=models.CharField(max_length=20,choices=ROLE_CHOICES)
    resume=models.FileField(upload_to='resumes/',null=True,blank=True)
    
