from django.contrib import admin
from .models import ResearchNotes,ResearchCompany,Investors
# Register your models here.

class ResearchNotesAdmin(admin.ModelAdmin):
  list_display = ['title','date_published','file_url']

class ResearchCompanyAdmin(admin.ModelAdmin):
  list_display = ['name','location','sector']

class InvestorAdmin(admin.ModelAdmin):
  list_display = ['name','email','partners']


admin.site.register(ResearchNotes,ResearchNotesAdmin)
admin.site.register(ResearchCompany,ResearchCompanyAdmin)
admin.site.register(Investors,InvestorAdmin)