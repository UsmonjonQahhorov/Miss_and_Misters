from rest_framework import permissions


class ServicePermision(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_verified
