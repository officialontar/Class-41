from django.db import models

# Create your models here.

class Job(models.Model):

    CATEGORY_CHOICES = [
        ('Part Time', 'Part Time'),
        ('Full Time', 'Full Time'),
        ('Remote Job', 'Remote Job'),
    ]

    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to='company_logo/', null=True, blank=True)

    respons = models.TextField()
    education = models.TextField()
    vacancies = models.PositiveIntegerField()

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField()
    skills = models.TextField()

    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()


    def __str__(self):
        return self.job_title
