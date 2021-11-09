from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class UsersConfig(AppConfig):
    name = 'api.apps.users'
    verbose_name = _('users')

    def ready(self):
        import api.apps.users.signals  # noqa