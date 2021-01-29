from core.models import Famoso, Cidade, Localiza
from datetime import date

def famcidata(famoso="", cidade="", data=""):
    if famoso!="" and cidade!="" and data=="":
        return Localiza.objects.filter(famoso__nome=famoso, cidade__nome=cidade)

    elif famoso!="" and cidade=="" and data!="":
        return Localiza.objects.filter(famoso__nome=famoso, data=date.fromisoformat(data))

    elif famoso=="" and cidade!="" and data!="":
        return Localiza.objects.filter(cidade__nome=cidade, data=date.fromisoformat(data))
