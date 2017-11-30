import codecs


class replacingSynonyms:
    def replacingSynonyms(self, tokensList):

        text = codecs.open('/home/erandi/PycharmProjects/SPD/Test/sample_synonyms.txt', 'r', 'utf-16').read()

        list = []
        for i in text:
            list = text.split(',')

        for i, tokens in enumerate(tokensList):
            for j, synonyms in enumerate(list):
                if (list[j] in tokensList[i]):
                    tokensList[i] = list[j]
        return tokensList
