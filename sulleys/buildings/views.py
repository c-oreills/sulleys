from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, RedirectView

from taggit.models import Tag

from buildings.models import Building



class BuildingList(ListView):
    model = Building


class BuildingListByTag(ListView):
    model = Building

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['tag'])
        return Building.objects.filter(tags=self.tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context


class BuildingDetail(DetailView):
    model = Building


class BuildingRedirectView(RedirectView):
    permanent = True
    query_string = True
    pattern_name = 'detail'

    def get(self, request, *args, **kwargs):
        self.building = get_object_or_404(Building, pk=kwargs['pk'])

        # Prevent infinite redirect loops
        if self.building.slug == str(self.building.pk):
            return BuildingDetail.as_view()(request, *args, **kwargs)

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(slug=self.building.slug)
