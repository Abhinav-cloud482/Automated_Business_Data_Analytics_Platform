import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from datasets.models import Dataset
from .models import AnomalyRun, DetectedAnomaly

@login_required
def anomaly_view(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk, user=request.user)
    file_path = dataset.cleaned_file.path if dataset.is_cleaned and dataset.cleaned_file else dataset.original_file.path
    df = pd.read_excel(file_path) if file_path.endswith(('.xlsx', '.xls')) else pd.read_csv(file_path)

    run, created = AnomalyRun.objects.get_or_create(dataset=dataset)
    if created:
        num_df = df.select_dtypes(include='number').dropna()
        if not num_df.empty and len(num_df) > 5:
            iso = IsolationForest(contamination=0.05, random_state=42)
            preds = iso.fit_predict(num_df)
            anomaly_indices = num_df.index[preds == -1]

            for idx in anomaly_indices[:15]: # Limit to 15 for demo
                DetectedAnomaly.objects.create(
                    run=run,
                    anomaly_type='Isolation Forest Outlier',
                    column_name=', '.join(num_df.columns[:2]),
                    record_index=int(idx),
                    detected_value=str(df.loc[idx, num_df.columns[0]]),
                    severity='High',
                    explanation='Multivariate anomaly detected via Isolation Forest.',
                    recommended_action='Investigate record for data entry error or exceptional business event.'
                )
        run.total_anomalies = run.anomalies.count()
        run.save()

    anomalies = run.anomalies.all()
    return render(request, 'anomaly_detection/anomaly.html', {
        'dataset': dataset,
        'run': run,
        'anomalies': anomalies
    })
