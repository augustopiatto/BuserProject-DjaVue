from core import views
from django.urls import path

urlpatterns = [
    path('api/dapau', views.dapau),
    path('api/login', views.login),
    path('api/logout', views.logout),
    path('api/signup', views.signup),
    path('api/mypage/<str:cidade>', views.mypage),
    path('api/addfamoso', views.add_famoso),
    path('api/addcidade', views.add_cidade),
    path('api/whoami', views.whoami),
    path('api/settings', views.settings),
    path('api/famosos', views.lista_famosos),
    path('api/fnome/<str:nome>', views.umfamoso),
    path('api/cnome/<str:nome>', views.umacidade),
    path('api/cidades', views.lista_cidades),
    path('api/<str:nome>', views.dawikipedia),
    path('api/localiza/famoso=<str:famoso>/cidade=<str:cidade>', views.localizaviews),
    path('api/localiza/famoso=<str:famoso>/data=<str:data>', views.localizaviews),
    path('api/localiza/cidade=<str:cidade>/data=<str:data>', views.localizaviews)
]
