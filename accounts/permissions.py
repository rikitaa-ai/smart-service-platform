from rest_framework.permissions import BasePermission


class IsOfficer(BasePermission):
    """
    Allows access only to users with OFFICER role.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "OFFICER"
        )