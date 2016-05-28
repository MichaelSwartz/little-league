from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Team, Player


class IndexView(generic.ListView):
    template_name = 'roster/index.html'

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


class PlayerCreate(generic.CreateView):
    model = Player
    template_name = 'roster/player_form.html'
    fields = ['name', 'active']

    def dispatch(self, *args, **kwargs):
        self.team = get_object_or_404(Team, pk=kwargs['team_id'])
        return super(PlayerCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.team = self.team
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    # def get_success_url(self):
    #     return reverse_lazy('roster:team', args=[str(self.team.id)])
