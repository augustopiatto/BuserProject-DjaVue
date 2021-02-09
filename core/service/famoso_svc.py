from core.models import Famoso
from core.service import localiza_svc

def adicionarfamoso(imagem, nome, descricao, wikip):
    famoso = Famoso.objects.create(imagem=imagem, nome=nome, descricao=descricao, wikip=wikip)
    localiza_svc.localpfamoso(famoso)
    return famoso.to_dict_json()

def lista_famosos():
    famoso = Famoso.objects.all()
    return famoso

def umfamoso(nome):
    famoso = Famoso.objects.get(nome=nome)
    return famoso

