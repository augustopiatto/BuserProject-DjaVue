# coding: utf-8
import json
import wikipedia
from django.http.response import HttpResponse, JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required
from core.service import log_svc, globalsettings_svc, localiza_svc, famoso_svc, cidade_svc
from django.views.decorators.csrf import csrf_exempt


def dapau(request):
    raise Exception('break on purpose')


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated:
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')


def signup(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(
        username=username, email=email, password=password)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.save()
    user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def add_famoso(request):
    imagem = request.FILES['imagem']
    nome = request.POST['nome']
    descricao = request.POST['descricao']
    wikipedia.set_lang("pt")
    wikip = wikipedia.summary(nome, sentences=5)
    famoso = famoso_svc.adicionarfamoso(
        imagem=imagem, nome=nome, descricao=descricao, wikip=wikip)
    return JsonResponse(famoso, safe=False)


def add_cidade(request):
    imagem = request.FILES['imagem']
    nome = request.POST['nome']
    descricao = request.POST['descricao']
    wikipedia.set_lang("pt")
    wikip = wikipedia.summary(nome, sentences=5)
    cidade = cidade_svc.adicionarcidade(
        imagem=imagem, nome=nome, descricao=descricao, wikip=wikip)
    return JsonResponse(cidade, safe=False)


def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated else {'authenticated': False}
    return JsonResponse(i_am)


def settings(request):
    le_settings = globalsettings_svc.list_settings()
    return JsonResponse(le_settings)


def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d

def umfamoso(request, nome):
    famoso = famoso_svc.umfamoso(nome)
    return JsonResponse(famoso.to_dict_json(), safe=False)

def umacidade(request, nome):
    cidade = cidade_svc.umacidade(nome)
    return JsonResponse(cidade.to_dict_json(), safe=False)


def lista_famosos(request):
    famosos= list(famoso_svc.lista_famosos())
    info= []
    for fam in famosos:
        info.append(fam.to_dict_json())
    return JsonResponse(info, safe=False)


def lista_cidades(request):
    cidades= list(cidade_svc.lista_cidades())
    info= []
    for cid in cidades:
        info.append(cid.to_dict_json())
    return JsonResponse(info, safe=False)


def dawikipedia(request, nome):
    wikipedia.set_lang("pt")
    a = {
        'content': wikipedia.summary(nome, sentences=5)
    }
    return JsonResponse(a, safe=False)


def localizaviews(request, famoso="", cidade="", data=""):
    localizaobjetos = list(localiza_svc.famcidata(famoso, cidade, data))
    info = []
    for obj in localizaobjetos:
        info.append(obj.to_dict_json())
    return JsonResponse(info, safe=False)
