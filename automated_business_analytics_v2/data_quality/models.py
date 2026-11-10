from django.db import models
from datasets.models import Dataset

class DataQualityAssessment(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='quality_assessments')
    overall_score = models.DecimalField(max_digits=5, decimal_places=2)
    completeness_score = models.DecimalField(max_digits=5, decimal_places=2)
    uniqueness_score = models.DecimalField(max_digits=5, decimal_places=2)
    validity_score = models.DecimalField(max_digits=5, decimal_places=2)
    consistency_score = models.DecimalField(max_digits=5, decimal_places=2)
    accuracy_score = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=50) # Excellent, Good, Moderate, Poor, Critical
    assessed_at = models.DateTimeField(auto_now_add=True)

class DataQualityIssue(models.Model):
    assessment = models.ForeignKey(DataQualityAssessment, on_delete=models.CASCADE, related_name='issues')
    dimension = models.CharField(max_length=50)
    column_name = models.CharField(max_length=255, blank=True, null=True)
    issue_description = models.TextField()
    severity = models.CharField(max_length=20)
    recommended_action = models.TextField(blank=True, null=True)
