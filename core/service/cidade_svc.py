from core.models import Cidade
from core.service import localiza_svc


def adicionarcidade(imagem, nome, descricao, wikip):
    cidade = Cidade.objects.create(
        imagem=imagem, nome=nome, descricao=descricao, wikip=wikip)
    localiza_svc.localpcidade(cidade)
    return cidade.to_dict_json()


def lista_cidades():
    cidade = Cidade.objects.all()
    return cidade


def umacidade(nome):
    cidade = Cidade.objects.get(nome=nome)
    return cidade
