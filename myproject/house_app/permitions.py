from rest_framework.permissions import BasePermission

class CheckRolePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'buyer'

class CreateHotelPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'seller'