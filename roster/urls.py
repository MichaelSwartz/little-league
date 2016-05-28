from django.conf.urls import url

from . import views

app_name = 'roster'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.TeamView.as_view(), name='team'),
    url(r'^create/$', views.TeamCreate.as_view(), name='team_form'),
    url(r'^(?P<team_id>[0-9]+)/add_player/$', views.PlayerCreate.as_view(), name='player_form'),
]
