from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('dashboard.urls')),
    path('datasets/', include('datasets.urls')),
    path('cleaning/', include('data_cleaning.urls')),
    path('quality/', include('data_quality.urls')),
    path('anomalies/', include('anomaly_detection.urls')),
    path('analytics/', include('analytics.urls')),
    path('ai-analyst/', include('ai_analyst.urls')),
    path('visualizations/', include('visualizations.urls')),
    path('executive-summary/', include('executive_summary.urls')),
    path('reports/', include('reports.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
