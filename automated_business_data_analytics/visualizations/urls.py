from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.visualization_view, name='visualization_view'),
]
