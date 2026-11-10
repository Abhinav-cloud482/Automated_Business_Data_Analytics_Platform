from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.anomaly_view, name='anomaly_view'),
]
