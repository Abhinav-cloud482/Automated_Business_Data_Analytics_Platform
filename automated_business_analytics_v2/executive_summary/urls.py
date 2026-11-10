from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.executive_summary_view, name='executive_summary_view'),
]
