from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Team(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Player(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Position(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Abilities(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    able = models.BooleanField(default=True)

    class Meta:
        unique_together = ('position', 'player')
