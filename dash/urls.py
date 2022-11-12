from . import views
from django.urls import path

urlpatterns = [
    path('', views.dash, name='dash-home'),
    path('about/', views.about, name='dash-about'),
]
