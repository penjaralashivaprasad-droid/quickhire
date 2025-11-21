from django.urls import path
from . import views
urlpatterns = [
    path('jobs/', views.JobListCreateView.as_view(), name='jobs_list_create'),
    path('jobs/<int:pk>/', views.JobRetrieveUpdateDestroyView.as_view(), name='job_rud'),
    path('jobs/<int:pk>/applicants/', views.JobApplicantsView.as_view(), name='job_applicants'),
    path('apply/', views.ApplyView.as_view(), name='apply_job'),
    path('myapplications/', views.MyApplicationsView.as_view(), name='my_applications'),
]
