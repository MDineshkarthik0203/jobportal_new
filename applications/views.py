from django.shortcuts import redirect,render
from rest_framework import viewsets
from .models import Application
from .serializers import ApplicationSerializer
from rest_framework.permissions import IsAuthenticated
from jobs.models import Job
from django.contrib import messages

def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)

    if not request.user.is_authenticated:
        return redirect('/login/')

    if Application.objects.filter(user=request.user, job=job).exists():
        return redirect('/')

    if request.method == "POST":
        print(request.POST)  # 🔥 DEBUG

        full_name = request.POST.get('full_name')
        resume = request.FILES.get('resume')

        # ✅ VALIDATION
        if not full_name or not resume:
            return render(request, 'apply.html', {
                'job': job,
                'error': 'All fields are required'
            })

        Application.objects.create(
            user=request.user,
            job=job,
            full_name=full_name,
            resume=resume
        )

        return redirect('/')

    return render(request, 'apply.html', {'job': job})

def job_applications(request, job_id):
    job = Job.objects.get(id=job_id)

    # only recruiter who created job
    if request.user != job.created_by:
        return redirect('/')

    applications = Application.objects.filter(job=job)

    return render(request, 'job_applications.html', {
        'applications': applications,
        'job': job
    })

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]