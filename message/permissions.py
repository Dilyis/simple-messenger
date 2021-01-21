from rest_framework import permissions


class MessagePermissions(permissions.BasePermission):
    """Permissions for MessageViewSet.
    """
    anonymous_actions = []
    authorized_actions = ['retrieve', 'create', 'list', 'destroy']

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
            view.action in self.authorized_actions and self._is_authenticated(
                request)
        ))

    def has_object_permission(self, request, view, obj):
        return all((
            self._is_admin(request) or self._is_authenticated(request),
            view.action in self.authorized_actions,
            request.user.id in (obj.sender.id, obj.receiver.id)
        ))
