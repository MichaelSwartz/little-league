from django.contrib import admin

from .models import Team, Player, Position, Ability, Game, Assignment

admin.site.register(Position)


class PlayerInline(admin.TabularInline):
    model = Player


class GameInline(admin.TabularInline):
    model = Game


class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInline, GameInline]


admin.site.register(Team, TeamAdmin)
