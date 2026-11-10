from django.db import models
from django.contrib.auth.models import User

class Dataset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='datasets')
    name = models.CharField(max_length=255)
    original_file = models.FileField(upload_to='datasets/raw/')
    cleaned_file = models.FileField(upload_to='datasets/cleaned/', blank=True, null=True)
    file_size = models.BigIntegerField()
    row_count = models.IntegerField(default=0)
    column_count = models.IntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_cleaned = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class CleaningHistory(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='cleaning_histories')
    operation_type = models.CharField(max_length=100)
    description = models.TextField()
    rows_affected = models.IntegerField(default=0)
    performed_at = models.DateTimeField(auto_now_add=True)
