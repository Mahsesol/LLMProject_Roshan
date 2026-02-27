from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ..models import Document


class DocumentRetriever:
    def retrieve(self, query, top_k=3):
        documents = list(Document.objects.all())

        if not documents:
            return ""

        corpus = [doc.content for doc in documents]

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(corpus)
        query_vector = vectorizer.transform([query])

        similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
        top_indices = similarities.argsort()[-top_k:][::-1]

        selected_docs = [documents[i] for i in top_indices]

        context = "\n\n".join(
            f"Title: {doc.title}\nContent: {doc.content}"
            for doc in selected_docs
        )

        return context
