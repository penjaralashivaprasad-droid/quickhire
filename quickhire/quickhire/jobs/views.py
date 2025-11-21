from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer
from .permissions import IsEmployer, IsApplicant
from django.db.models import Q
class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated(), IsEmployer()]
        return [permissions.IsAuthenticated()]
    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get('search')
        loc = self.request.query_params.get('location')
        if q:
            qs = qs.filter(title__icontains=q)
        if loc:
            qs = qs.filter(location__icontains=loc)
        return qs
    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)
class JobRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    def get_permissions(self):
        if self.request.method in ('PUT','DELETE'):
            return [permissions.IsAuthenticated(), IsEmployer()]
        return [permissions.IsAuthenticated()]
    def perform_update(self, serializer):
        job = self.get_object()
        if job.posted_by != self.request.user:
            return Response({'detail':'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
        serializer.save()
    def perform_destroy(self, instance):
        if instance.posted_by != self.request.user:
            return Response({'detail':'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
        instance.delete()
class JobApplicantsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]
    def get_queryset(self):
        job = generics.get_object_or_404(Job, pk=self.kwargs['pk'])
        if job.posted_by != self.request.user:
            return Application.objects.none()
        return job.applications.all()
class ApplyView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsApplicant]
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['applicant'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        # enforce unique constraint handled by model's unique_together
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)
class MyApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsApplicant]
    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user).order_by('-applied_at')
