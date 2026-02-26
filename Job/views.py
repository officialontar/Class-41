from django.shortcuts import redirect, render, get_object_or_404
from .models import Job
from django.contrib import messages
from django.db.models import Q


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
    sort = request.GET.get('sort')  # 'asc' or 'desc'

    all_jobs = Job.objects.all()

    if sort == 'asc':
        all_jobs = all_jobs.order_by('job_title')
    elif sort == 'desc':
        all_jobs = all_jobs.order_by('-job_title')

    context = {
        'jobs': all_jobs,
        'sort': sort
    }

    return render(request, 'Jobs/all_jobs.html', context)


def browse_jobs(request):

    browse_jobs = Job.objects.all()

    context = {
        'jobs': browse_jobs
    }


    query = request.GET.get('q')

    if query:
        jobs = Job.objects.filter(
            Q(job_title__icontains=query) |
            Q(company_name__icontains=query) |
            Q(category__icontains=query) |
            Q(location__icontains=query) |
            Q(deadline__icontains=query) 
        )
    else:
        jobs = Job.objects.all()

    context = {
        'jobs': jobs,
        'query': query
    }

    return render(request, 'Jobs/browse_jobs.html', context)


def signle_job_view(request, job_id):
    job_data = get_object_or_404(Job, id=job_id)

    context = {
        'job': job_data
    }

    return render(request, 'Jobs/signle_job_view.html', context)


def edit_job(request, job_id):

    job_data = get_object_or_404(Job, id=job_id)

    if request.method == "POST":
        job_data.job_title = request.POST.get('title')
        job_data.company_name = request.POST.get('company_name')

        if request.FILES.get('company_logo'):
            job_data.company_logo = request.FILES.get('company_logo')

        job_data.respons = request.POST.get('respons')
        job_data.education = request.POST.get('education')
        job_data.vacancies = request.POST.get('vacancies')
        job_data.category = request.POST.get('category')
        job_data.description = request.POST.get('description')
        job_data.skills = request.POST.get('skills')
        job_data.location = request.POST.get('location')
        job_data.deadline = request.POST.get('deadline')

        job_data.save()

        messages.success(request, 'Data Update Successfully !')
        return redirect('all_jobs')

    context = {
        'job': job_data
    }

    return render(request, 'Jobs/edit_job.html', context)



def delete_job(request, job_id):

    job = Job.objects.filter(Job, id=job_id)
    job.delete()


    messages.success(request, ('Job Successfully Deleted !!!'))

    return redirect('all_jobs')