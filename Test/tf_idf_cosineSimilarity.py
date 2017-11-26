 # -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import codecs

train_set = ["The sky is blue.", "The sun is bright.", "The sun is in the sky."] #Documents
test_set = ["The sun in the sky is bright."] #Query
stopWords = stopwords.words('english')

vectorizer = CountVectorizer(stop_words = stopWords)
#print vectorizer
transformer = TfidfTransformer()
#print transformer

trainVectorizerArray = vectorizer.fit_transform(train_set).toarray()
testVectorizerArray = vectorizer.transform(test_set).toarray()
print 'Fit Vectorizer to train set', trainVectorizerArray
print 'Transform Vectorizer to test set', testVectorizerArray

transformer.fit(trainVectorizerArray)
print
print transformer.transform(trainVectorizerArray).toarray()

transformer.fit(testVectorizerArray)
print
tfidf = transformer.transform(testVectorizerArray)
print tfidf.todense()


f = open("para1.txt")
doc1 = str.decode(f.read(), "UTF-8", "ignore")
f = open("para2")
doc2 = str.decode(f.read(), "UTF-8", "ignore")
f = open("para3")
doc3 = str.decode(f.read(), "UTF-8", "ignore")

sentence = u'කැමරාව පමණක් අතැතිවය. මෙම ගමනේ අතිශය දුෂ්කර'.encode('utf-8') # unicode to str("කැමරාව පමණක් අතැතිවය. මෙම ගමනේ අතිශය දුෂ්කර")
train_set = [sentence,doc1, doc2, doc3]

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix_train = tfidf_vectorizer.fit_transform(train_set)  #finds the tfidf score with normalization
print "cosine scores ==> ",cosine_similarity(tfidf_matrix_train[0:1], tfidf_matrix_train)  #here the first element of tfidf_matrix_train is matched with other three elements