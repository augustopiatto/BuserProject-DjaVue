from core.models import Famoso, Cidade, Localiza
from datetime import date, timedelta

def famcidata(famoso="", cidade="", data=""):
    if famoso!="" and cidade!="" and data=="":
        return Localiza.objects.filter(famoso__nome=famoso, cidade__nome=cidade)

    elif famoso != "" and cidade == "" and data != "":
        datacerta = Localiza.objects.filter(
            famoso__nome=famoso, data=date.fromisoformat(data))
        if datacerta.exists():
            return datacerta
        else:
            datas = Localiza.objects.filter(famoso__nome=famoso)
            items = []
            for obj in datas:
                items.append(obj.data)
            pivot = date.fromisoformat(data)
            datamin = min(items, key=lambda x: abs(x - pivot))
        return Localiza.objects.filter(famoso__nome=famoso, data=datamin)

    elif famoso=="" and cidade!="" and data!="":
        datacerta = Localiza.objects.filter(
            cidade__nome=cida, data=date.fromisoformat(data))
        if datacerta.exists():
            return datacerta
        else:
            datas = Localiza.objects.filter(cidade__nome=cidade)
            items = []
            for obj in datas:
                items.append(obj.data)
            pivot = date.fromisoformat(data)
            datamin = min(items, key=lambda x: abs(x - pivot))
        return Localiza.objects.filter(cidade__nome=cidade, data=datamin)


def localpfamoso(famoso):
    localizas = Localiza.objects.all().order_by('data').reverse()
    d = localizas[0]
    i = 1
    for cid in Cidade.objects.all():
        Localiza.objects.create(
            famoso=famoso, cidade=cid, data=d.data+timedelta(days=i))
        i += 1


def localpcidade(cidade):
    localizas = Localiza.objects.all().order_by('data').reverse()
    d = localizas[0]
    i = 1
    for fam in Famoso.objects.all():
        Localiza.objects.create(
            famoso=fam, cidade=cidade, data=d.data+timedelta(days=i))
        i += 1
