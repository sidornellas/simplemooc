from django.conf.urls import url, include, patterns

urlpatterns = [
    url(r'^$', 'simplemooc.core.views.home', name='home'),
    url(r'^contato/$', 'simplemooc.core.views.contact', name='contact'),
]
