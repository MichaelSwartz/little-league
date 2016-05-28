from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.forms import ModelForm
from django.views import generic

from .models import Team, Player, Game, Position, Assignment


#############
### FORMS ###
#############


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name']

   # def __init__(self, *args, **kwargs):
   #     self.request = kwargs.pop('request', None)
   #     return super(TeamForm, self).__init__(*args, **kwargs)

   # def save(self, *args, **kwargs):
   #     kwargs['commit'] = False
   #     team = super(TeamForm, self).save(*args, **kwargs)
   #     if self.request:
   #         team.owner = self.request.user
   #     team.save()
   #     return team


def index(request):
    teams = Team.objects.order_by('name')
    return render(request, 'roster/index.html', {'teams': teams})


def team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render(request, 'roster/team.html', {'team': team})

def team_create(request):
    form = TeamForm(request.POST or None)
    team = form.save(commit=False)
    team.owner = request.user
    if form.is_valid():
        team.save()
        return HttpResponseRedirect(reverse('roster:team', args=(team.id,)))

    return render(request, 'roster/team_form.html', {'form': form})


# class TeamCreate(generic.CreateView):
#     model = Team
#     template_name = 'roster/team_form.html'
#     fields = ['name', 'owner']


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



class GameCreate(generic.CreateView):
    model = Game
    template_name = 'roster/game_form.html'
    fields = ['date', 'opponent']

    def dispatch(self, *args, **kwargs):
        self.team = get_object_or_404(Team, pk=kwargs['team_id'])
        return super(GameCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.team = self.team
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class GameView(generic.DetailView):
    model = Game
    template_name = 'roster/game.html'

    def get_queryset(self):
        return Game.objects
