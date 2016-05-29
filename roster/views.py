from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.forms import ModelForm
from django.views import generic

from .models import Team, Player, Game, Position, Assignment


### FORMS ###


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name']


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'active']


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['date', 'opponent']

### Teams ###

def index(request):
    teams = Team.objects.order_by('name')
    return render(request, 'roster/index.html', {'teams': teams})

def team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render(request, 'roster/team.html', {'team': team})

def team_create(request):
    form = TeamForm(request.POST or None)
    if form.is_valid():
        team = form.save(commit=False)
        team.owner = request.user
        team.save()
        return HttpResponseRedirect(reverse('roster:team', args=(team.id,)))

    return render(request, 'roster/team_form.html', {'form': form})

def player_create(request, team_id):
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        team = get_object_or_404(Team, pk=team_id)
        player = form.save(commit=False)
        player.team = team
        player.save()
        return HttpResponseRedirect(reverse('roster:team', args=(team_id,)))

    return render(request, 'roster/player_form.html', {'form': form})

### Games ###

def game_create(request, team_id):
    form = GameForm(request.POST or None)
    if form.is_valid():
        team = get_object_or_404(Team, pk=team_id)
        game = form.save(commit=False)
        game.team = team
        game.save()
        return HttpResponseRedirect(reverse('roster:game', args=(game.pk,)))

    return render(request, 'roster/game_form.html', {'form': form})

def game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'roster/game.html', {'game': game})
