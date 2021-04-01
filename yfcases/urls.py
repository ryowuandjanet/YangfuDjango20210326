from django.urls import path
from . import views

app_name='yfcase'
 
urlpatterns = [
  path('', views.HomePageView.as_view(), name='home'),
  path('yfcase/new/',views.YfcaseCreateView.as_view(),name="yfcase_new"),
  path('ajax/load-townships/', views.load_townships, name='ajax_load_townships'),
]
