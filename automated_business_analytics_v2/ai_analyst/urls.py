from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ai_analyst_view, name='ai_analyst_view'),
]
