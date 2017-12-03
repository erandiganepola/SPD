import io


class RemovingStopWords:
    def removeStopwords(self, tokensList):
        fin = io.open("Preprocessor/resources/stopWordList.txt", "r", encoding='utf-8').read().replace('\n', ' ')
        return [token for token in tokensList if token not in fin]
