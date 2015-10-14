from django.contrib.gis.geos import fromstr
from django.views.generic import DetailView
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.contrib.gis.measure import D

from app.forms import SweetForm, GeoSweetForm
from app.models import Sweet


class HomeView(TemplateView):

    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['add_form'] = SweetForm()
        context['around_you_form'] = GeoSweetForm()
        return context

class AddFormView(FormView):
    template_name = 'app/home.html'
    form_class = SweetForm

    def form_valid(self, form):
        obj = Sweet(
            sweet=form.cleaned_data['sweet'],
            point = fromstr("POINT(%s %s)" % (
                form.cleaned_data['longitude'],
                form.cleaned_data['latitude']))
        )
        obj.save()
        self.obj = obj
        return super(AddFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse('sweet', kwargs={'pk':self.obj.pk})


class AroundYouFormView(FormView):
    template_name = 'app/fake_template.html'
    form_class = GeoSweetForm

    def form_valid(self, form):
        point = (form.cleaned_data['longitude'],
                 form.cleaned_data['latitude']
        )
        self.request.session['point'] = point
        return super(AroundYouFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse('around_you_view')


class SweetDetail(DetailView):
    model = Sweet

    def get_context_data(self, **kwargs):
        context = super(SweetDetail, self).get_context_data(**kwargs)
        context['sweets'] = Sweet.objects.filter(
            point__distance_lte=(self.object.point, D(m=50))
        ).exclude(id=self.object.id)
        return context


class AroundYouView(ListView):
    model = Sweet
    template_name = 'app/sweet_list'
    context_object_name='sweets'

    def get_queryset(self):
        point = fromstr("POINT(%s %s)" % tuple(self.request.session['point']))
        self.queryset = Sweet.objects.filter(
            point__distance_lte=(point, D(m=50)))
        return super(AroundYouView, self).get_queryset()
