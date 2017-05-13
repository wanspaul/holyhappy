from rest_framework.permissions import BasePermission
from django.core.urlresolvers import resolve


class CustomPermission(BasePermission):

    def has_permission(self, request, view):
        return True

