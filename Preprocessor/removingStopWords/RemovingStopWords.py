import io
import os


class RemovingStopWords:
    def removeStopwords(self, tokensList):
        infile = os.path.dirname(os.path.abspath(__file__)) + "/../resources/stopWordList.txt"
        fin = io.open(infile, "r", encoding='utf-8').read().replace('\n', ' ')

        for i, j in enumerate(tokensList):
            if j in fin:
                tokensList[i] = ""
        return tokensList
