from django.urls import path
from api import views

urlpatterns = [
   path('currencies/', views.currencies),
   # path('convert_currencies', views.convert_currency),
]