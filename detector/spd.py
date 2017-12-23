from sklearn.feature_extraction.text import TfidfVectorizer

from Preprocessor.removingStopWords.RemovingStopWords import RemovingStopWords
from Preprocessor.removingUnnecessaryChars.removeUnnecessaryChars import removeUnnecessaryChars
from Preprocessor.replacingSynonyms.ReplacingSynonyms import ReplacingSynonyms
from Preprocessor.stemming.StemmingSinhala import StemmingSinhala
from Preprocessor.tokenizing.TokenizeText import TokenizeText


class SPD:
    @staticmethod
    def standardize(doc):
        text = doc
        print("Input: %r" % text)

        # TODO replace text between quotation marks by replacing with ""

        remove_unnecessary = removeUnnecessaryChars()
        text = remove_unnecessary.removePunctuation(text)
        print("Removed punctuations: %r" % text)

        text = remove_unnecessary.replaceNumbers(text)
        print("Numbers replaced: %r" % text)

        tokenizer = TokenizeText()
        tokens_list = tokenizer.tokenizeText(text)
        print("Tokens: %r" % tokens_list)

        stop_words_remover = RemovingStopWords()
        output = stop_words_remover.removeStopwords(tokens_list)
        tokens_list = output
        print("Removed stop words: %r" % output)

        replaced_synonyms = ReplacingSynonyms()
        synonyms_replaced_list = replaced_synonyms.replacingSynonyms(tokens_list)
        tokens_list = synonyms_replaced_list
        print("Synonym replaced: %r" % synonyms_replaced_list)

        print("Standardized Text: %r" % " ".join(tokens_list))

        stemming = StemmingSinhala()
        tokens_list = stemming.stem(tokens_list)
        print("Stemmed: %r" % tokens_list)

        standardized_text = " ".join(tokens_list);
        print("Standardized Text: %r" % standardized_text)
        return standardized_text

    @staticmethod
    def compare(docs):
        documents = [doc for doc in docs]
        tf_idf = TfidfVectorizer().fit_transform(documents)
        # no need to normalize, since Vectorizer will return normalized tf-idf
        pairwise_similarity = tf_idf * tf_idf.T
        similarities = pairwise_similarity.toarray().tolist()
        print(similarities)
        return similarities

    @staticmethod
    def compare_uploaded_files(files):
        tf_idf = TfidfVectorizer().fit_transform(files)
        # no need to normalize, since Vectorizer will return normalized tf-idf
        pairwise_similarity = tf_idf * tf_idf.T
        similarities = pairwise_similarity.toarray().tolist()
        print(similarities)
        uniqueness = SPD.find_uniqueness(similarities)
        return uniqueness

    @staticmethod
    def find_uniqueness(similarity_list):
        result_list = []
        count = len(similarity_list) - 1

        for index in range(0, len(similarity_list)):
            similarities = [x for i, x in enumerate(similarity_list[index]) if i != index]
            uniqueness = round(1 - max(similarities), 2)

            print(uniqueness)
            result_list.append(uniqueness)

        return result_list
