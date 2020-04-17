from django.contrib import admin
from djangoapp.models import Computer
class ComputerAdmin(admin.ModelAdmin):
    list_display = ['computer_name','IP_address','MAC_address','users_name','location','price','purchase_date','timestamp']
# class OperatingAdmin(admin.ModelAdmin):
#     list_display = ['operating_system']

admin.site.register(Computer,ComputerAdmin)
# admin.site.register(Operating_system,OperatingAdmin)
