from django.contrib.auth.models import Group, User
from rest_framework import serializers
from django.contrib.admin.models import LogEntry

from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Permission

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

class LogEntrySerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    content_type = serializers.StringRelatedField()
    action = serializers.SerializerMethodField()
    class Meta:
        model = LogEntry
        fields = [
            "id",
            "action_time",
            "user",
            "content_type",
            "object_repr",
            "action",
            "change_message",
        ]
    def get_action(self, obj):
        return {
            1: "Added",
            2: "Changed",
            3: "Deleted",
        }.get(obj.action_flag, "Unknown")
    
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ["id", "name", "content_type"]

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ["session_key", "expire_date", "decoded_data"]

    decoded_data = serializers.SerializerMethodField()

    def get_decoded_data(self, obj):
        return obj.get_decoded()    


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = ["id", "app_label", "model"]

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ["key", "user", "created"]

                         