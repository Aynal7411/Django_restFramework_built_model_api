from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Snippet
        fields = [
            "id",
            "owner",
            "title",
            "code",
            "linenos",
            "language",
            "style",
            "created",
        ]
        read_only_fields = ["id", "created", "owner"]
