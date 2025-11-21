from django.contrib import admin
from .models import Job, Application
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title','location','salary','posted_by','created_at')
    search_fields = ('title','location','posted_by__username')
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job','applicant','status','applied_at')
    list_filter = ('status',)
    search_fields = ('applicant__username','job__title')
