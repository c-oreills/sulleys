from django.shortcuts import render

from django.views.generic import DetailView, ListView
from buildings.models import Building


class BuildingList(ListView):
    model = Building


class BuildingDetail(DetailView):
    model = Building
