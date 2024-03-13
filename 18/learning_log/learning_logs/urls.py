from django.urls import path

from . import views

urlpatterns = [
    # main page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name="topic")
]
