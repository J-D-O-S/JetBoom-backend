from django.shortcuts import render
from django.views.generic import TemplateView


class LugaresTuristicosView(TemplateView):
    template_name = "lugaresTuristicos.html"


class AlbumFotosView(TemplateView):
    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ["album/album_authenticated.html"]
        else:
            return ["album_nologin.html"]

    # template_name = "album.html"
