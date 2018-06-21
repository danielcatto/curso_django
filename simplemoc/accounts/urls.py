from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'simplemoc.accounts.views.dashboard',
        name='dashboard'),

    url(r'^entrar/$', 'django.contrib.auth.views.login',
        {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', 'django.contrib.auth.views.logout',
        {'next_page': 'core:home'}, name='logout'),
    url(r'^cadastre-se/$', 'simplemoc.accounts.views.register',name='register'),
    url(r'^editar/$', 'simplemoc.accounts.views.edit',name='edit'),

)

