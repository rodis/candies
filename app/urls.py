from django.conf.urls import include, url
from django.contrib import admin

from app.views import manage_sweet, SweetLists


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', manage_sweet),
    url(r'^sweets/$', SweetLists.as_view(), name='sweets'),
]
