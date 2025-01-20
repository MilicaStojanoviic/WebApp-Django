from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin): #ovako sam sortirala kako s=ce se prikazivati lista stranica na admin panelu
   list_display = ('title','update_date')
   ordering = ('title',)
   search_fields = ('title',)

admin.site.register(Page,PageAdmin) #ovako modelu moze da pristupi admin, registovano je
