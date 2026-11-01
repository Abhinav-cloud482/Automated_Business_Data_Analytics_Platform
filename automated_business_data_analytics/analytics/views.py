import pandas as pd
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from datasets.models import Dataset

@login_required
def eda_view(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk, user=request.user)
    file_path = dataset.cleaned_file.path if dataset.is_cleaned and dataset.cleaned_file else dataset.original_file.path
    df = pd.read_excel(file_path) if file_path.endswith(('.xlsx', '.xls')) else pd.read_csv(file_path)

    overview = {
        'rows': df.shape[0],
        'columns': df.shape[1],
        'missing_values': int(df.isnull().sum().sum()),
        'duplicates': int(df.duplicated().sum()),
        'memory': f"{df.memory_usage(deep=True).sum() / 1024:.2f} KB"
    }

    desc_stats = df.describe(include='all').fillna('-').to_html(classes='table table-bordered table-sm')

    num_df = df.select_dtypes(include='number')
    corr_html = num_df.corr().round(3).to_html(classes='table table-striped table-sm') if not num_df.empty else "<p class='text-muted'>No numerical columns available for correlation matrix.</p>"

    insights = []
    if not num_df.empty:
        for col in num_df.columns:
            mean_val = num_df[col].mean()
            max_val = num_df[col].max()
            min_val = num_df[col].min()
            insights.append(f"Column <strong>{col}</strong> ranges from {min_val:.2f} to {max_val:.2f} with an average of {mean_val:.2f}.")

    return render(request, 'analytics/eda.html', {
        'dataset': dataset,
        'overview': overview,
        'desc_stats': desc_stats,
        'corr_html': corr_html,
        'insights': insights
    })
