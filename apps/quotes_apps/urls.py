from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
    url(r'^quotes$', views.quotes),
    url(r'^users/(?P<id>\d+)$', views.profile),
    # url(r'^users/add/(?P<id>\d+)$', views.add_friend),
    # url(r'^users/remove/(?P<id>\d+)$', views.remove_friend),
]