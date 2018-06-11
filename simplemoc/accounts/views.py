from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .forms import RegisterForm
# Create your views here.

#usamas a classe RegisterForm que herda de UserCreationForm criado no forms.py que tem os formulario de autenticação do django e
# acrecentamos o email ou (alguma informação a mais)
def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        #antes era
        #form = UserCreationForm(request.POST)
        #e foi criado arquivo forms e criado a class RegistrerForm que herda de registerForms
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, template_name, context)