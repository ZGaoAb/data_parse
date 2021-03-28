from django.urls import path
from . import views

urlpatterns = [
    path('index', views.temperatrue, name='temperatrue'),
    path('show_co2/<int:year>/', views.show_co2, name='show_co2'),

]