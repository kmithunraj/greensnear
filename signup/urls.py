from django.urls import path
from . import views


urlpatterns = [
    path('', views.signuppg, name='signup'),
]