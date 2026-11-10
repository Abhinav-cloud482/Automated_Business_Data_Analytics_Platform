from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datasets.models import Dataset
from data_quality.models import DataQualityAssessment
from anomaly_detection.models import AnomalyRun

@login_required
def dashboard_view(request):
    datasets = Dataset.objects.filter(user=request.user).order_by('-uploaded_at')
    total_datasets = datasets.count()
    total_records = sum([d.row_count for d in datasets])
    recent_datasets = datasets[:5]

    # Calculate average quality score across user datasets
    assessments = DataQualityAssessment.objects.filter(dataset__user=request.user)
    avg_quality = round(sum([a.overall_score for a in assessments]) / assessments.count(), 1) if assessments.exists() else 0.0

    total_anomalies = AnomalyRun.objects.filter(dataset__user=request.user).aggregate(models.Sum('total_anomalies'))['total_anomalies__sum'] or 0

    return render(request, 'dashboard/index.html', {
        'total_datasets': total_datasets,
        'total_records': total_records,
        'avg_quality': avg_quality,
        'total_anomalies': total_anomalies,
        'recent_datasets': recent_datasets
    })
