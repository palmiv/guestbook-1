from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^´$', views.Index, name='Index')
    #url(r'^(?P<pk>[0-9]+)/entry/$', views.EntryView.as_view(), name='entry'),

]
