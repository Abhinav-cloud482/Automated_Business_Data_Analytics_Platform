from django.db import models
from django.contrib.auth.models import User
from datasets.models import Dataset

class AIConversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ai_conversations')
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='ai_conversations')
    title = models.CharField(max_length=255, default='Analytics Session')
    created_at = models.DateTimeField(auto_now_add=True)

class AIMessage(models.Model):
    conversation = models.ForeignKey(AIConversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=20) # 'user' or 'ai'
    message_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
