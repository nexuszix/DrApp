from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from dbapi import views

urlpatterns = [
    url(r'^drmas/$', views.dr_list),
    url(r'^drmas/(?P<pk>.+)$', views.dr_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)