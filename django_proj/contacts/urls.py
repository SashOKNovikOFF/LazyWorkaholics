from django.urls import path, include

from contacts import views

urlpatterns = [
    path('', views.index, name='index'),
]
