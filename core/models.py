from django.db import models
from django.contrib.auth.models import User

class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser", on_delete=models.SET_NULL)
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )

class Famoso(models.Model):
    descricao = models.CharField(max_length=512, null=True)
    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="media", blank=True, null=True)
    wikip = models.CharField(max_length=5000, null=True)

    def to_dict_json(self):
        return {
            'descricao': self.descricao,
            'nome': self.nome,
            'imagem': self.imagem.url,
            'wikip': self.wikip
        }

class Cidade(models.Model):
    descricao = models.CharField(max_length=512, null=True)
    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="media", blank=True, null=True)
    wikip = models.CharField(max_length=5000, null=True)

    def to_dict_json(self):
        return {
            'descricao': self.descricao,
            'nome': self.nome,
            'imagem': self.imagem.url,
            'wikip': self.wikip
        }

class Localiza(models.Model):
    famoso = models.ForeignKey(Famoso, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    data = models.DateField()
    
    def to_dict_json(self):
        return {
            'famoso': self.famoso.nome,
            'fimagem': self.famoso.imagem.url,
            'cidade': self.cidade.nome,
            'data': self.data.isoformat()
        }


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


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    cidade = models.CharField(max_length=100, null=True)

    def to_dict_json(self):
        return {
            'user': _user2dict(self.user),
            'cidade': self.cidade
        }
