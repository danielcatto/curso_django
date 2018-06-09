from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'status']
    #define os campos para realizar pesquisas
    search_fields = ['name', 'status']

admin.site.register(Contact, ContactAdmin)