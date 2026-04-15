from django.urls import path
from . import views

app_name = 'home'

# Enrutamiento para la página principal
urlpatterns = [
    path('', views.index, name='home'),
]