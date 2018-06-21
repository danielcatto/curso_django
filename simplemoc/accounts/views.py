from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.conf import settings
from .forms import RegisterForm, EditAccountForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    return render(request, template_name)


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
            user = form.save()
            user = authenticate(username = user.username, password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('core:home')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, template_name, context)

def edit(request):
    template_name = 'accounts/edit.html'
    form = EditAccountForm()
    context = {}
    context['form'] = form
    return render(request, template_name, context)