'''
Aqui se faz o cadastramento dos Models
primeiro faz-se o import do Modelo
'''
from django.contrib import admin
from .models import  Course

#esta class interfere no models Course na area do admin, mostrando todos os campos da tabela
#é necessario incluir no admin.site.register
class CourseAdmin(admin.ModelAdmin):
    #mostra todos os campos da tabela
    list_display = ['name', 'slug', 'start_date', 'created_at']
    #define os campos para realizar pesquisas
    search_fields = ['name', 'slug']
    #automatiza o preenchimento do campo slug no form de cadastro
    #Um dicionário com o campo para preenchimento, com uma lista dos campos de referencia
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Course, CourseAdmin)