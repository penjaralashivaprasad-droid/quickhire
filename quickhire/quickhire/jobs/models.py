from django.db import models
from accounts.models import User
class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=200)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
class Application(models.Model):
    STATUS_CHOICES = (('pending','Pending'),('shortlisted','Shortlisted'),('rejected','Rejected'),('hired','Hired'))
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    resume_link = models.URLField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('job','applicant')
    def __str__(self):
        return f"{self.applicant.username} -> {self.job.title} ({self.status})"
