from django.contrib import admin

# Register your models here.
from .models import gamesAnalyzed
from .models import bestPractices

admin.site.register(gamesAnalyzed)
admin.site.register(bestPractices)