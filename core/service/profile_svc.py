from core.models import Profile
from django.shortcuts import get_object_or_404


def sign_up(User, cidade):
    usuario = Profile.objects.create(user=User, cidade=cidade)
    return usuario


def cidade(user):
    if user.is_anonymous:
        return {}
    else:
        return Profile.objects.get(user=user)
