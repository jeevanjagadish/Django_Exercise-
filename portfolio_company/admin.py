from django.contrib import admin
from portfolio_company.models import Founders,News,Category,PortfolioCompany

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
  list_display = ['company_name','category','show_in_recent_investment','show_on_portfolio_page']
class NewsAdmin(admin.ModelAdmin):
  list_display = ['portfolio','display_order_id','publisher','publish_date','headline']
admin.site.register(PortfolioCompany,PortfolioAdmin)
admin.site.register(Category)
admin.site.register(Founders)
admin.site.register(News,NewsAdmin)
