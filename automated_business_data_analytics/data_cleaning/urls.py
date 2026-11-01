from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.cleaning_view, name='cleaning_view'),
]
