
from django.contrib import admin
from django.urls import path,include

from rest_framework import routers

from user_app.views import GroupViewSet, UserViewSet,LogEntryViewSet,PermissionViewSet,SessionViewSet,ContentTypeViewSet
from snippets.views import SnippetViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'logentries', LogEntryViewSet, basename='logentry')
router.register(r'permissions', PermissionViewSet, basename='permission')
router.register(r'sessions', SessionViewSet, basename='session')
router.register(r'contenttypes', ContentTypeViewSet, basename='contenttype')
router.register(r'snippets', SnippetViewSet, basename='snippet')


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
