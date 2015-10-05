from django.conf.urls import include, url
from django.contrib import admin

from app.views import SweetDetail, SweetFormView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', SweetFormView.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$', SweetDetail.as_view(), name='sweet'),
]
