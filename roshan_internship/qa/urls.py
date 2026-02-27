from django.urls import path
from .views import ask_question, add_document

urlpatterns = [
    path("ask/", ask_question),
    path("documents/add/", add_document),
]
