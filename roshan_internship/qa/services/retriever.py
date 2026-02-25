from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from roshan_internship.qa.models import Document


class TfidfRetriever:

    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words="english")

    def retrieve(self, query, top_k=3):
        documents = Document.objects.all()

        if not documents.exists():
            return []

        corpus = [doc.content for doc in documents]
        tfidf_matrix = self.vectorizer.fit_transform(corpus)
        query_vec = self.vectorizer.transform([query])

        similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
        ranked_indices = similarities.argsort()[-top_k:][::-1]

        return [documents[i] for i in ranked_indices]