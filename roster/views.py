from django.core.urlresolvers import reverse_lazy, reverse

from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Team


class IndexView(generic.ListView):
    template_name = 'roster/index.html'
    # context_object_name = 'team_list'

    def get_queryset(self):
        return Team.objects.order_by('name')


class TeamView(generic.DetailView):
    model = Team
    template_name = 'roster/team.html'

    def get_queryset(self):
        return Team.objects


class TeamCreate(generic.CreateView):
    model = Team
    template_name = 'roster/team_form.html'
    fields = ['name', 'owner']
    # success_url = reverse_lazy('roster:index')
