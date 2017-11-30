# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import codecs


class CalculateTf_idf_CosineSimilarity:
    def calculateTf_idf(self, text):
        doc1 = codecs.open('/home/erandi/PycharmProjects/SPD/Test/para2.txt', 'r', 'utf-16').read()
        doc2 = codecs.open('/home/erandi/PycharmProjects/SPD/Test/para3.txt', 'r', 'utf-16').read()

        searchDoc = codecs.open('/home/erandi/PycharmProjects/SPD/Test/para1.txt', 'r', 'utf-16').read()
        train_set = [searchDoc, doc1, doc2]

        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix_train = tfidf_vectorizer.fit_transform(train_set)  # finds the tfidf score with normalization

        return tfidf_matrix_train

        def calculateSimilarityScore(self, tfidf_matrix_train):
            # here the first element of tfidf_matrix_train is matched with other three elements
            print("cosine scores ==> ", cosine_similarity(tfidf_matrix_train[0:1],
                                                          tfidf_matrix_train))
