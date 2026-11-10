from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.quality_view, name='quality_view'),
]
