from .retriever import TfidfRetriever
from .llm import LocalLLM


class QAPipeline:

    def __init__(self):
        self.retriever = TfidfRetriever()
        self.llm = LocalLLM()

    def run(self, question_text: str):
        documents = self.retriever.retrieve(question_text)

        context = "\n\n".join([doc.content for doc in documents])

        prompt = f"""
You are a helpful assistant.
Answer only using the provided context.
If the answer is not in the context, say you do not know.

Context:
{context}

Question:
{question_text}

Answer:
"""

        answer = self.llm.generate(prompt)

        return answer, context