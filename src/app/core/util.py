from rest_framework.reverse import reverse


class Enum:
    ALL = {}

    @classmethod
    def choices(cls):
        return list(cls.ALL.items())


class ViewSetTestMixin:
    """
    How to use:
        1) Inherit from the class
        2) Override the `_basename` attribute
        3) Use the `self.reverse_view_url()` function

    Examples of usage for common actions:
        url = self.reverse_view_url('create')
        url = self.reverse_view_url('destroy', pk=1)
        url = self.reverse_view_url('list')
        url = self.reverse_view_url('retrieve', pk=1)
        url = self.reverse_view_url('partial_update', pk=1)
        url = self.reverse_view_url('update', pk=1)

        url = self.reverse_view_url('custom_action_name')

    """
    _basename = None

    @classmethod
    def _get_view_name(cls, action_name):
        if action_name in ('list', 'create'):
            action = 'list'
        elif action_name in ('retrieve', 'update', 'partial_update', 'destroy'):
            action = 'detail'
        else:
            action = action_name

        return '%s-%s' % (cls._basename, action)

    @classmethod
    def reverse_view_url(cls, action=None, request=None, **kwargs):
        """Reverses view url for `self._basename` and given action.

        For list of default actions,
        see http://www.django-rest-framework.org/api-guide/routers/#simplerouter

        Raises `django.urls.NoReverseMatch`, if it's unable to reverse the url.
        """
        view_name = cls._basename if action is None else cls._get_view_name(
            action)
        return reverse(view_name, kwargs=kwargs, request=request)

