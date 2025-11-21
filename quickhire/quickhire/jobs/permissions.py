from rest_framework.permissions import BasePermission
class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and getattr(request.user,'role',None) == 'employer')
class IsApplicant(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and getattr(request.user,'role',None) == 'applicant')
