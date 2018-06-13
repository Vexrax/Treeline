from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views




urlpatterns = [
    path('', views.index, name='index'),
    url('champion/', views.handle_search, name='handle_search'),
    url('test', views.load_rune_page, name='test_page')
]