from django.contrib import admin
from .models import Document, Question


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "tags")
    search_fields = ("title", "content", "tags")


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "created_at")
    readonly_fields = ("answer_text", "retrieved_context")
