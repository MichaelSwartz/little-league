from django.conf.urls import url

from . import views

app_name = 'roster'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<team_id>[0-9]+)/$', views.team, name='team'),
    url(r'^create/$', views.team_create, name='team_form'),
    url(r'^(?P<team_id>[0-9]+)/add_player/$', views.player_create, name='player_form'),
    url(r'^(?P<team_id>[0-9]+)/new_game/$', views.game_create, name='game_form'),
    url(r'^game/(?P<game_id>[0-9]+)/$', views.game, name='game'),
]
