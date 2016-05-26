from django.views import generic

from .models import Team


class IndexView(generic.ListView):
    template_name = 'roster/index.html'

    def get_queryset(self):
        return Team.objects.order_by('name')
