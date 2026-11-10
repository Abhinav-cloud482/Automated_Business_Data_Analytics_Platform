import os
import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datasets.models import Dataset, CleaningHistory

@login_required
def cleaning_view(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk, user=request.user)
    file_path = dataset.cleaned_file.path if dataset.is_cleaned and dataset.cleaned_file else dataset.original_file.path
    df = pd.read_excel(file_path) if file_path.endswith(('.xlsx', '.xls')) else pd.read_csv(file_path)

    if request.method == 'POST':
        action = request.POST.get('action')
        desc = ""
        rows_before = len(df)

        if action == 'drop_missing':
            df = df.dropna()
            desc = "Dropped all rows containing missing values."
        elif action == 'fill_mean':
            num_cols = df.select_dtypes(include='number').columns
            df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
            desc = "Imputed missing numerical values with column means."
        elif action == 'fill_median':
            num_cols = df.select_dtypes(include='number').columns
            df[num_cols] = df[num_cols].fillna(df[num_cols].median())
            desc = "Imputed missing numerical values with column medians."
        elif action == 'fill_mode':
            for col in df.columns:
                if not df[col].mode().empty:
                    df[col] = df[col].fillna(df[col].mode()[0])
            desc = "Imputed missing values using mode strategy."
        elif action == 'remove_duplicates':
            df = df.drop_duplicates()
            desc = "Removed duplicate rows across all columns."
        elif action == 'strip_whitespace':
            str_cols = df.select_dtypes(include=['object', 'string']).columns
            for col in str_cols:
                df[col] = df[col].str.strip()
            desc = "Normalized text by removing leading/trailing whitespaces."

        rows_after = len(df)
        rows_affected = rows_before - rows_after

        cleaned_dir = os.path.join(os.path.dirname(dataset.original_file.path), '..', 'cleaned')
        os.makedirs(cleaned_dir, exist_ok=True)
        cleaned_path = os.path.join(cleaned_dir, f"cleaned_{dataset.pk}.csv")
        df.to_csv(cleaned_path, index=False)

        dataset.cleaned_file.name = f"datasets/cleaned/cleaned_{dataset.pk}.csv"
        dataset.is_cleaned = True
        dataset.row_count = len(df)
        dataset.save()

        CleaningHistory.objects.create(
            dataset=dataset,
            operation_type=action,
            description=desc,
            rows_affected=rows_affected
        )
        return redirect('cleaning_view', pk=dataset.pk)

    histories = dataset.cleaning_histories.all().order_by('-performed_at')
    preview = df.head(10).to_html(classes='table table-striped table-hover', index=False)
    return render(request, 'data_cleaning/cleaning.html', {'dataset': dataset, 'preview': preview, 'histories': histories})
