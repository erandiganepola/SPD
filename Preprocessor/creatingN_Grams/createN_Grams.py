from nltk import ngrams


class createN_Grams:
    def createN_Grams(self, text, ngramValue):
        ngramArray = []
        n = ngramValue
        trigrams = ngrams(text.split(), n)
        for grams in trigrams:
            ngramArray.append(grams)
        return ngramArray
