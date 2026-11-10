import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Dataset

@login_required
def dataset_list(request):
    datasets = Dataset.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'datasets/list.html', {'datasets': datasets})

@login_required
def dataset_upload(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        file = request.FILES.get('file')
        if file:
            df = pd.read_excel(file) if file.name.endswith(('.xlsx', '.xls')) else pd.read_csv(file)
            row_count, column_count = df.shape
            dataset = Dataset.objects.create(
                user=request.user,
                name=name or file.name,
                original_file=file,
                file_size=file.size,
                row_count=row_count,
                column_count=column_count
            )
            return redirect('dataset_detail', pk=dataset.pk)
    return render(request, 'datasets/upload.html')

@login_required
def dataset_detail(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk, user=request.user)
    file_path = dataset.original_file.path
    df = pd.read_excel(file_path) if file_path.endswith(('.xlsx', '.xls')) else pd.read_csv(file_path)
    preview = df.head(10).to_html(classes='table table-striped table-hover', index=False)
    summary = {
        'columns': list(df.columns),
        'dtypes': df.dtypes.astype(str).to_dict(),
        'missing': df.isnull().sum().to_dict(),
        'duplicates': int(df.duplicated().sum()),
    }
    return render(request, 'datasets/detail.html', {'dataset': dataset, 'preview': preview, 'summary': summary})

@login_required
def dataset_delete(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk, user=request.user)
    dataset.delete()
    return redirect('dataset_list')
