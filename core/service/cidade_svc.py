from core.models import Cidade

def adicionarcidade(imagem, nome, descricao, wikip):
    cidade = Cidade.objects.create(imagem=imagem, nome=nome, descricao=descricao, wikip=wikip)
    return cidade.to_dict_json()

def lista_cidades():
    cidade = Cidade.objects.all()
    return cidade

def umacidade(nome):
    cidade = Cidade.objects.get(nome=nome)
    return cidade