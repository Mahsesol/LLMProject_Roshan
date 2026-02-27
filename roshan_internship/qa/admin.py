from django.contrib import admin
from .models import Document, Question


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "tags")
    search_fields = ("title", "content", "tags")
    list_filter = ("created_at",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("short_question", "created_at")
    readonly_fields = ("answer_text", "retrieved_context")
    search_fields = ("question_text",)

    def short_question(self, obj):
        return obj.question_text[:60]
