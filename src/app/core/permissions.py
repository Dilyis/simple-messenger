from rest_framework import permissions


class BaseCustomPermission(permissions.BasePermission):
    """Base permission
    """
    anonymous_actions = ()
    authorized_actions = ()

    @staticmethod
    def _is_authenticated(request):
        return request.user and request.user.is_authenticated

    @classmethod
    def _is_admin(cls, request):
        return cls._is_authenticated(request) and request.user.is_superuser

    def has_permission(self, request, view):
        return any((
            self._is_admin(request),
            view.action in self.anonymous_actions,
            view.action in self.authorized_actions and self._is_authenticated(request)
        ))
