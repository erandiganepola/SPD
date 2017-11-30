from nltk import ngrams


class CreateN_Grams:
    def createN_Grams(self, list, ngramValue):
        ngramArray = []
        n = ngramValue

        trigrams = ngrams(list, n)
        for grams in trigrams:
            ngramArray.append(grams)

        return ngramArray
