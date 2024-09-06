from django.shortcuts import render
from django.views.generic import TemplateView


class AlbumFotosView(TemplateView):
    template_name = "album.html"
