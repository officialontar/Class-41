from django.contrib import admin
from django.utils.html import format_html
from .models import Job


# Register your models here.
# admin.site.register(Job)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_title', 'company_name', 'company_logo', 'respons', 'education', 'vacancies', 'CATEGORY_CHOICES', 'description', 'skills', 'location', 'deadline', 'created_at')
    list_filter = ('id', 'job_title', 'company_name', 'company_logo', 'category',)
    search_fields = ('job_title', 'company_name', 'category', 'location')
    ordering = ('id', '-created_at',)
    readonly_fields = ('logo_preview',)



    def logo_preview(self, obj):
        if obj.company_logo:
            return format_html(
                '<a href="{}" target="_blank">'
                '<img src="{}" width="50" height="50" style="object-fit:cover; border-radius:5px;" />'
                '</a>',
                obj.company_logo.url,
                obj.company_logo.url
            )
        return "No Logo"

    logo_preview.short_description = "Company Logo"