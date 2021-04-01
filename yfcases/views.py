from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from .models import *
from users.models import *
from .forms import *

class HomePageView(TemplateView):
  template_name = 'home.html'

class YfcaseCreateView(CreateView):
  model=Yfcase
  form_class = YfcaseForm
  template_name="yfcase/yfcase_new.html"
  success_url = reverse_lazy('yfcase:home')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['value'] = '建立'
    context['title'] = '新增基本資料'
    return context

def load_townships(request):
  city_id = request.GET.get('city')
  townships = Township.objects.filter(city_id=city_id).order_by('name')
  return render(request, 'yfcase/township_dropdown_list_options.html', {'townships': townships})
