from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='yfcase'
 
urlpatterns = [
  path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
  path('', views.YfcaseListView.as_view(), name='home'),
  path('yfcase/new/',views.YfcaseCreateView.as_view(),name="yfcase_new"),
  path('ajax/load-townships/', views.load_townships, name='ajax_load_townships'),
]
