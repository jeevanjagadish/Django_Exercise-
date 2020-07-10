from django.contrib import admin
from .models import TeamMember
# Register your models here.
class Team(admin.ModelAdmin):
    list_display = ( "name", "position","order_id")

admin.site.register(TeamMember,Team)


