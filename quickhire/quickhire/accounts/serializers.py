from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('username','email','password','role')
    def validate(self, data):
        if data.get('role') not in ('employer','applicant'):
            raise serializers.ValidationError({'role':'Role must be employer or applicant'})
        return data
    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data['email'], role=validated_data['role'])
        user.set_password(validated_data['password'])
        user.save()
        return user
