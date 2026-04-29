# /LLMProject_Roshan/roshan_internship/qa/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Question, Document
from .services.qa_pipeline import QAPipeline


@api_view(["POST"])
def ask_question(request):
    question_text = request.data.get("question")

    if not question_text:
        return Response(
            {"error": "Question field is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    pipeline = QAPipeline()
    answer, context = pipeline.run(question_text)

    Question.objects.create(
        question_text=question_text,
        answer_text=answer,
        retrieved_context=context
    )

    return Response({
        "question": question_text,
        "answer": answer
    })


@api_view(["POST"])
def add_document(request):
    title = request.data.get("title")
    content = request.data.get("content")
    tags = request.data.get("tags", "")

    if not title or not content:
        return Response(
            {"error": "Title and content are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    doc = Document.objects.create(
        title=title,
        content=content,
        tags=tags
    )

    return Response({
        "message": "Document created",
        "id": doc.id
    })
