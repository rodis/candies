from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import ListView

from app.models import Sweet
from app.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$', SweetDetail.as_view(), name='sweet'),
    url(r'^add_form/$',
        AddFormView.as_view(),
        name='add_form'
    ),
    url(r'^around_you_form/$',
        AroundYouFormView.as_view(),
        name='around_you_form'
    ),
    url(r'^sweets/$',
        ListView.as_view(
            model=Sweet,
            queryset=Sweet.objects.all(),
            template_name='app/sweet_list.html',
            context_object_name='sweets',
        ),
        name='sweet_list'
    ),
    url(r'^sweets_around_you/$',
        AroundYouView.as_view(),
        name='around_you_view'
    ),
]
