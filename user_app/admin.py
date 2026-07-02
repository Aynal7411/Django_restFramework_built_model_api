from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Permission

# ---------------- LOG ENTRY ----------------
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "action_time",
        "user",
        "content_type",
        "object_repr",
        "action_flag",
    )

    list_filter = ("action_flag", "content_type")
    search_fields = ("object_repr",)

    def has_add_permission(self, request):
        return False


# ---------------- SESSION ----------------
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("session_key", "expire_date", "decoded_data")

    def decoded_data(self, obj):
        return obj.get_decoded()

    decoded_data.short_description = "Session Data"


# ---------------- CONTENT TYPE ----------------
@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "app_label", "model")
    search_fields = ("app_label", "model")
    list_filter = ("app_label",)


# ---------------- TOKEN ----------------

class TokenAdmin(admin.ModelAdmin):
    list_display = ("key", "user", "created")
    search_fields = ("key", "user__username")
    list_filter = ("created",)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "content_type")
    search_fields = ("name",)
    list_filter = ("content_type",)