from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, "index.html")


class MyCustomPageNotFoundView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "404.html", {}, status=404)
