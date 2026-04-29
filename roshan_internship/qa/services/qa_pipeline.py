#LLMProject_Roshan/roshan_internship/qa/services/qa_pipeline.py

from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

from .retriever import DocumentRetriever
from .llm import get_llm


class QAPipeline:
    def __init__(self):
        self.retriever = DocumentRetriever()

        self.prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
                        You are a helpful assistant.
                        Answer only using the provided context.
                        If the answer is not in the context, say you do not know.

                        Context:
                        {context}

                        Question:
                        {question}

                        Answer:
                        """,
        )

        self.chain = LLMChain(llm=get_llm(), prompt=self.prompt)

    def run(self, question):
        context = self.retriever.retrieve(question)

        # answer = self.chain.invoke(
        #     {"context": context, "question": question}
        # )["text"]
        result = self.chain.invoke({"context": context, "question": question})

        print("DEBUG RESULT:", result)

        answer = result.get("text") or result.get("output_text") or str(result)

        return answer, context