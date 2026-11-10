import pandas as pd
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from datasets.models import Dataset
from .models import DataQualityAssessment, DataQualityIssue

@login_required
def quality_view(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk, user=request.user)
    file_path = dataset.cleaned_file.path if dataset.is_cleaned and dataset.cleaned_file else dataset.original_file.path
    df = pd.read_excel(file_path) if file_path.endswith(('.xlsx', '.xls')) else pd.read_csv(file_path)

    total_cells = df.size if df.size > 0 else 1
    total_missing = df.isnull().sum().sum()
    completeness = max(0.0, 100.0 * (1.0 - (total_missing / total_cells)))

    total_rows = len(df)
    unique_rows = len(df.drop_duplicates())
    uniqueness = 100.0 * (unique_rows / total_rows) if total_rows > 0 else 100.0

    validity = 95.0  # Placeholder proxy for type validity
    consistency = 90.0 # Placeholder proxy for format consistency
    accuracy = 85.0 # Placeholder proxy for logical validity

    overall = (completeness * 0.25) + (uniqueness * 0.20) + (validity * 0.20) + (consistency * 0.20) + (accuracy * 0.15)

    status = 'Excellent'
    if overall < 40: status = 'Critical'
    elif overall < 60: status = 'Poor'
    elif overall < 75: status = 'Moderate'
    elif overall < 90: status = 'Good'

    assessment, _ = DataQualityAssessment.objects.update_or_create(
        dataset=dataset,
        defaults={
            'overall_score': round(overall, 2),
            'completeness_score': round(completeness, 2),
            'uniqueness_score': round(uniqueness, 2),
            'validity_score': round(validity, 2),
            'consistency_score': round(consistency, 2),
            'accuracy_score': round(accuracy, 2),
            'status': status
        }
    )

    return render(request, 'data_quality/quality.html', {
        'dataset': dataset,
        'assessment': assessment
    })
