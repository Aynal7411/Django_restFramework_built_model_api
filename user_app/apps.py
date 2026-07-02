from django.apps import AppConfig


class UserAppConfig(AppConfig):
    name = 'user_app'
    verbose_name = "User Management system"
    def ready(self):
        import user_app.admin_site