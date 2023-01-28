from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepg, name='home'),
]