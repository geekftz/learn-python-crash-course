from django.urls import path

from . import views

urlpatterns = [
    # main page
    # re_path(r'^$', views.index, name='index'),
    path('', views.index, name='index')
]
