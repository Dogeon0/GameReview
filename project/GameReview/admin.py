from django.contrib import admin

# Register your models here.
from . import models

class GameReviewAdmin(admin.ModelAdmin):
    list_display = ("titulo","autor")
    list_display_links = ("titulo",)
admin.site.register(models.GameReview,GameReviewAdmin)