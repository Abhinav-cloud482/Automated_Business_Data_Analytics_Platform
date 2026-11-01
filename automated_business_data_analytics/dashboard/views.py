from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datasets.models import Dataset

@login_required
def dashboard_view(request):
    user_datasets = Dataset.objects.filter(user=request.user).order_by('-uploaded_at')
    total_datasets = user_datasets.count()
    total_records = sum([d.row_count for d in user_datasets])
    recent_datasets = user_datasets[:5]

    return render(request, 'dashboard/index.html', {
        'total_datasets': total_datasets,
        'total_records': total_records,
        'recent_datasets': recent_datasets
    })
