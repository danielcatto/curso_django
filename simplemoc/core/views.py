from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # o render deve ser passado o 'request' , 'arquivo html', 'um dicionario de variaveis'
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')