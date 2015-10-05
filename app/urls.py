from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import ListView

from app.models import Sweet
from app.views import SweetDetail, SweetFormView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', SweetFormView.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$', SweetDetail.as_view(), name='sweet'),
    url(r'^sweets/$',
        ListView.as_view(
            model=Sweet,
            queryset=Sweet.objects.all(),
            template_name='app/sweet_list.html',
            context_object_name='sweets',
        ),
        name='sweet_list'),
]
