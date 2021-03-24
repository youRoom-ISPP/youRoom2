from django.shortcuts import render
from django.views.generic import TemplateView
from publicacion.models import Publicacion
from usuario.models import UsuarioPerfil


class PerfilView(TemplateView):
    template_name = 'perfil/perfil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario, create = UsuarioPerfil.objects.get_or_create(user = self.request.user)
        context['publicaciones'] = Publicacion.objects.filter(usuario=usuario)
        context['user'] = usuario
        return context