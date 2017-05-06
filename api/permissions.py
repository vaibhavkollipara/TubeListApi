from rest_framework.permissions import BasePermission
from myauth.models import SiteUser


class IsPlaylistOwner(BasePermission):

    message = "Sorry ! You don't have access for that"

    def has_object_permission(self, request, view, obj):
        user = SiteUser.objects.get(username=request.user.username)
        return user == obj.created_by


class IsCurrentUser(BasePermission):
    message = "You don't have access for that"

    def has_object_permission(self, request, view, obj):
        user = SiteUser.objects.get(username=request.user.username)
        return user == obj


class IsMyPlylistVideo(BasePermission):

    message = "Sorry ! You don't have access for that"

    def has_object_permission(self, request, view, obj):
        user = SiteUser.objects.get(username=request.user.username)
        return obj.playlist.created_by == user
