from django.conf.urls import url
from django.contrib import admin

from .views import home_page, contact_page, about_page


urlpatterns = [
    url(r'^$', home_page),
    url(r'^contact/$', contact_page),
    url(r'^about/$', about_page),
]