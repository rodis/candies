from django.contrib.gis.geos import fromstr
from django.views.generic import DetailView
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.contrib.gis.measure import D

from app.forms import SweetForm
from app.models import Sweet


class SweetFormView(FormView):
    template_name = 'home.html'
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
        return super(SweetFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse('sweet', kwargs={'pk':self.obj.pk})


class SweetDetail(DetailView):
    model = Sweet

    def get_context_data(self, **kwargs):
        context = super(SweetDetail, self).get_context_data(**kwargs)
        context['sweets'] = Sweet.objects.filter(
            point__distance_lte=(self.object.point, D(m=50))).exclude(id=self.object.id)
        return context
