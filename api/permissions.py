from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Allow read-only for anyone. Write is allowed for the author or staff.
    """
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (hasattr(obj, "author") and obj.author == request.user) or request.user.is_staff
