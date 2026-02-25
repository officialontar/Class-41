from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Job

# Create your views here.

def home(request):

    return render(request, 'Jobs/index.html')

def add_job(request):
    if request.method == "POST":
        title = request.POST.get('title', '').strip()
        company_name = request.POST.get('company_name', '').strip()
        company_logo = request.FILES.get('company_logo')
        respons = request.POST.get('respons', '').strip()
        education = request.POST.get('education', '').strip()
        category = request.POST.get('category', '').strip()
        description = request.POST.get('description', '').strip()
        skills = request.POST.get('skills', '').strip()
        location = request.POST.get('location', '').strip()
        deadline = request.POST.get('deadline', '').strip()

        # Vacancies safe convert
        vacancies_raw = request.POST.get('vacancies', '').strip()
        try:
            vacancies = int(vacancies_raw)
        except ValueError:
            vacancies = None

        # Simple validation (minimum)
        if not title or not company_name or vacancies is None or vacancies <= 0 or not category or not deadline:
            messages.error(request, "Please fill required fields correctly (Title, Company, Vacancies, Category, Deadline).")
            return redirect('add_job')

        # Save
        Job.objects.create(
            job_title=title,
            company_name=company_name,
            company_logo=company_logo,
            respons=respons,
            education=education,
            vacancies=vacancies,
            category=category,
            description=description,
            skills=skills,
            location=location,
            deadline=deadline
        )

        messages.success(request, "Job Successfully Added!")
        return redirect('all_jobs')

    return render(request, 'Jobs/add_job.html')


def all_jobs(request):

    all_jobs = Job.objects.all()

    context = {
        'jobs': all_jobs
    }


    return render(request, 'Jobs/all_jobs.html', context)