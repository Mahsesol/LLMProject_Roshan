# /LLMProject_Roshan/roshan_internship/qa/models.py
from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return self.title


class Question(models.Model):
    question_text = models.TextField()
    answer_text = models.TextField(blank=True, null=True)
    retrieved_context = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text[:60]
