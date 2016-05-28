from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse_lazy, reverse


@python_2_unicode_compatible
class Team(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('roster:team', args=[str(self.id)])


@python_2_unicode_compatible
class Player(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('roster:team', args=[str(self.team.id)])


@python_2_unicode_compatible
class Position(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Ability(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    able = models.BooleanField(default=True)

    class Meta:
        unique_together = ('position', 'player')

    def __str__(self):
        return "{} {} {}".format(self.player, self.position, self.able)

    def get_absolute_url(self):
        return reverse('roster:team', args=[str(self.player.team.id)])


@python_2_unicode_compatible
class Game(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.DateField()
    opponent = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        unique_together = ('date', 'team', 'opponent')

    def __str__(self):
        opponent = (" against " + str(self.opponent)) if self.opponent else ""
        return "{} - {}{}".format(self.date, self.team.name, opponent)

    def get_absolute_url(self):
        return reverse('roster:team', args=[str(self.team.id)])

@python_2_unicode_compatible
class Assignment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    inning = models.IntegerField()

    class Meta:
        unique_together = (('game', 'inning', 'player'),
                           ('game', 'inning', 'position'))

    def __str__(self):
        return "{} {} {}".format(self.inning, self.position, self.player)

    def get_absolute_url(self):
        return reverse('roster:team', args=[str(self.player.team.id)])
