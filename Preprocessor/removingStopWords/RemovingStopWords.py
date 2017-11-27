import io
import os


class RemovingStopWords:
    def removeStopwords(self, text):
        infile = os.path.dirname(os.path.abspath(__file__)) + "/../resources/stopWordList.txt"
        fin = io.open(infile, "r", encoding='utf-8').read().replace('\n', ' ')

        # print fin
        text = text.lower()
        words = text.split()
        words.sort()

        for word in words:
            if word in fin:
                text = text.replace(word, "")
                # print text
        return text
