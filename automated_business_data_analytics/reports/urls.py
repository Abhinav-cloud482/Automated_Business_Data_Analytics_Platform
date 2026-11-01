from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/download-csv/', views.download_cleaned_csv, name='download_cleaned_csv'),
]
