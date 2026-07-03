from rest_framework import permissions, viewsets
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows snippets to be viewed or edited.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.AllowAny]
