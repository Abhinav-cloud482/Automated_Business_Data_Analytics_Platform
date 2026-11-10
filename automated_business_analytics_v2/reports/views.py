import pandas as pd
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from datasets.models import Dataset

@login_required
def download_cleaned_csv(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk, user=request.user)
    file_path = dataset.cleaned_file.path if dataset.is_cleaned and dataset.cleaned_file else dataset.original_file.path
    df = pd.read_excel(file_path) if file_path.endswith(('.xlsx', '.xls')) else pd.read_csv(file_path)
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="cleaned_{dataset.name}.csv"'
    df.to_csv(response, index=False)
    return response
