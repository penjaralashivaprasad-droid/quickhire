from rest_framework import serializers
from .models import Job, Application
class JobSerializer(serializers.ModelSerializer):
    posted_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ('posted_by','created_at','updated_at')
class ApplicationSerializer(serializers.ModelSerializer):
    applicant = serializers.StringRelatedField(read_only=True)
    job = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all())
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ('applicant','applied_at')
