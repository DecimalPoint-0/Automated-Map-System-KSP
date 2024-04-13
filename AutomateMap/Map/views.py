# from pyexpat import model
from urllib import request
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
# from numpy import place

from .models import Place

def service(request):
    return render(request, "map/service.html")


# Create your views here.
class Index(ListView):
    template_name = "map/index.html"
    context_object_name = "places"
    def get_queryset(self):
        return Place.objects.all()

    def post(self, request):
        name = request.POST.get("place")
        places = Place.objects.all()
        s_place = Place.objects.get(pk=int(name))
        return render(request, self.template_name, {'s_place': s_place, 'places': places})

