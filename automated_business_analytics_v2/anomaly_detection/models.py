from django.db import models
from datasets.models import Dataset

class AnomalyRun(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='anomaly_runs')
    total_anomalies = models.IntegerField(default=0)
    run_at = models.DateTimeField(auto_now_add=True)

class DetectedAnomaly(models.Model):
    run = models.ForeignKey(AnomalyRun, on_delete=models.CASCADE, related_name='anomalies')
    anomaly_type = models.CharField(max_length=100)
    column_name = models.CharField(max_length=255, blank=True, null=True)
    record_index = models.IntegerField(blank=True, null=True)
    detected_value = models.TextField(blank=True, null=True)
    severity = models.CharField(max_length=20)
    explanation = models.TextField()
    recommended_action = models.TextField()
    is_reviewed = models.BooleanField(default=False)
