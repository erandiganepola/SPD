import codecs

from Preprocessor.removingStopWords.RemovingStopWords import RemovingStopWords
from Preprocessor.stemming.StemmingSinhala import StemmingSinhala
from Preprocessor.creatingN_Grams.createN_Grams import createN_Grams

from Preprocessor.removingUnnecessaryChars.removeUnnecessaryChars import removeUnnecessaryChars

if __name__ == '__main__':
    text = codecs.open('Test/para1.txt', 'r', 'utf-16').read()
    print(text)

    removeUnnecessary = removeUnnecessaryChars()
    output = removeUnnecessary.removePunctuation(text)
    text = output
    print(text)

    output = removeUnnecessary.replaceNumbers(text)
    text = output
    print(text)

    stopWords = RemovingStopWords()
    output = stopWords.removeStopwords(text)
    text = output
    print(text)

    nGrams = createN_Grams()
    output = nGrams.createN_Grams(text, 3)
    print(output)

    stemming = StemmingSinhala()
    #last = stemming.stemminig(output.split())
    #print(last)
