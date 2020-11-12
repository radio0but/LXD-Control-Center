from django.urls import path

from . import views

urlpatterns = [
    path('', views.button, name='Home'),
    path('output',views.output, name="output"),
]