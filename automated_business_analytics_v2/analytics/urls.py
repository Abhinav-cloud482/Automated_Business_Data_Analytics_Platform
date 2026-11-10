from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.eda_view, name='eda_view'),
]
