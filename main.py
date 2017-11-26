import codecs

from Preprocessor.removingStopWords.RemovingStopWords import RemovingStopWords
from Preprocessor.stemming.StemmingSinhala import StemmingSinhala

from Preprocessor.removingUnnecessaryChars.removeUnnecessaryChars import removeUnnecessaryChars

if __name__ == '__main__':
    text = codecs.open('Test/para1.txt', 'r', 'utf-16').read()
    print(text)

    stopWords = RemovingStopWords()
    output = stopWords.removeStopwords(text)
    print(output)

    removeUnnecessary = removeUnnecessaryChars()
    output = removeUnnecessary.removeChars(output)

    print(output)

    stemming = StemmingSinhala()
    last = stemming.stemminig(output.split())

    print(last)
