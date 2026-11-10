import pandas as pd
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from datasets.models import Dataset

@login_required
def executive_summary_view(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk, user=request.user)
    file_path = dataset.cleaned_file.path if dataset.is_cleaned and dataset.cleaned_file else dataset.original_file.path
    df = pd.read_excel(file_path) if file_path.endswith(('.xlsx', '.xls')) else pd.read_csv(file_path)

    summary = {
        'total_records': len(df),
        'total_columns': len(df.columns),
        'missing_cells': int(df.isnull().sum().sum()),
        'duplicates': int(df.duplicated().sum())
    }

    recommendations = [
        "Monitor data completeness regularly to maintain analytical precision.",
        "Review identified outliers before finalizing executive forecasts.",
        "Leverage the AI Conversational Analyst to drill down into specific regional or departmental KPIs."
    ]

    return render(request, 'executive_summary/summary.html', {
        'dataset': dataset,
        'summary': summary,
        'recommendations': recommendations
    })
