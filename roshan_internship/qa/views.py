from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Question
from .services.qa_pipeline import QAPipeline


@api_view(["POST","GET"])
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