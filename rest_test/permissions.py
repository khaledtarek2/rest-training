from rest_framework import permissions


class IsCarOwner(permissions.BasePermission):
    # for object level permissions
    def has_object_permission(self, request, view, car_obj):
        return car_obj.owner.id == request.user.id