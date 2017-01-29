from django.conf.urls import url
from dbapi import views

urlpatterns = [
    url(r'^drmas/$', views.dr_list),
    url(r'^drmas/(?P<pk>.+)/$', views.dr_detail),
]