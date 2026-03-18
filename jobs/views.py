from django.shortcuts import render,redirect
from .models import Job
from rest_framework import viewsets
from .serializers import JobSerializer
from rest_framework.permissions import IsAuthenticated
from applications.models import Application

# Create your views here.
def job_list(request):
    jobs = Job.objects.all()

    applied_jobs = []

    if request.user.is_authenticated:
        applied_jobs = Application.objects.filter(user=request.user).values_list('job_id', flat=True)

    return render(request, 'job_list.html', {
        'jobs': jobs,
        'applied_jobs': applied_jobs
    })

def add_job(request):
    if not request.user.is_authenticated:
        return redirect('/login/')

    if request.method == "POST":
        Job.objects.create(
            title=request.POST.get('title'),
            company=request.POST.get('company'),
            location=request.POST.get('location'),
            salary=request.POST.get('salary'),
            description=request.POST.get('description'),
            created_by=request.user
        )
        return redirect('/')

    return render(request, 'add_job.html')

def recruiter_jobs(request):
    if request.user.role != 'recruiter':
        return redirect('/')

    jobs = Job.objects.filter(created_by=request.user)
    return render(request, 'recruiter_jobs.html', {'jobs': jobs})


class JobViewSet(viewsets.ModelViewSet):
    queryset=Job.objects.all()
    serializer_class=JobSerializer
    permission_classes=[IsAuthenticated]