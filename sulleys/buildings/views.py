from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from taggit.models import Tag

from buildings.models import Building



class BuildingList(ListView):
    model = Building


class BuildingListByTag(ListView):
    model = Building

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['tag'])
        return Building.objects.filter(tags=self.tag)


class BuildingDetail(DetailView):
    model = Building
