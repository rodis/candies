from django.contrib.gis.geos import fromstr
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import ListView
from django.core.urlresolvers import reverse

from app.forms import SweetForm
from app.models import Sweet


def manage_sweet(request):
    if request.method == "POST":
        formset = SweetForm(request.POST, request.FILES)
        # import ipdb; ipdb.set_trace()
        if formset.is_valid():
            obj = Sweet(
                sweet=formset.cleaned_data['sweet'],
                point = fromstr("POINT(%s %s)" % (
                    formset.cleaned_data['longitude'],
                    formset.cleaned_data['latitude']))
            )
            obj.save()
            return HttpResponseRedirect(reverse('sweets'))
    else:
        formset = SweetForm()
    return render(request, "home.html", {'formset': formset})


class SweetLists(ListView):
    model = Sweet
