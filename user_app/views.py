from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from django.contrib.admin.models import LogEntry
from user_app.serializers import GroupSerializer, UserSerializer,LogEntrySerializer,PermissionSerializer,SessionSerializer,ContentTypeSerializer, TokenSerializer
from django.contrib.auth.models import Permission
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class LogEntryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LogEntry.objects.select_related(
        "user", "content_type"
    ).all().order_by("-action_time")

    serializer_class = LogEntrySerializer  

class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Permission.objects.select_related(
        "content_type"
    ).all().order_by("name")

    serializer_class = PermissionSerializer    

class SessionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Session.objects.all().order_by("-expire_date")
    serializer_class = SessionSerializer

class ContentTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContentType.objects.all().order_by("model")
    serializer_class = ContentTypeSerializer    

