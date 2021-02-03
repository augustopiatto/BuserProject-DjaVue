from core.models import Localiza
from datetime import date


def mypage(cidade):
    return Localiza.objects.filter(cidade__nome=cidade)
