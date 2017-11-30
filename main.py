import codecs

from Preprocessor.removingStopWords.RemovingStopWords import RemovingStopWords
from Preprocessor.stemming.StemmingSinhala import StemmingSinhala
from Preprocessor.creatingN_Grams.CreateN_Grams import CreateN_Grams
from Preprocessor.tokenizing.TokenizeText import TokenizeText
from Preprocessor.replacingSynonyms.replacingSynonyms import replacingSynonyms
#from SimilarityComparissor.calculateTf_idf_CosineSimilarity import calculateTf_idf_CosineSimilarity

from Preprocessor.removingUnnecessaryChars.removeUnnecessaryChars import removeUnnecessaryChars

if __name__ == '__main__':
    text = codecs.open('Test/para1.txt', 'r', 'utf-16').read()
    print(text)

    # TODO replace text between quotation marks by replacing with ""

    removeUnnecessary = removeUnnecessaryChars()
    output = removeUnnecessary.removePunctuation(text)
    text = output
    print(text)

    output = removeUnnecessary.replaceNumbers(text)
    text = output
    print(text)

    tokens = TokenizeText()
    tokensList = tokens.tokenizeText(text)
    print(tokensList)

    stopWords = RemovingStopWords()
    output = stopWords.removeStopwords(tokensList)
    tokensList = output
    print(output)

    replacedSynonyms = replacingSynonyms()
    synonymsReplacedList = replacedSynonyms.replacingSynonyms(tokensList)
    tokensList = synonymsReplacedList
    print(synonymsReplacedList)

    nGrams = CreateN_Grams()
    output = nGrams.createN_Grams(tokensList, 3)
    tokensList = output
    print(output)

    #stemming = StemmingSinhala()
    #standardizedTextList = stemming.stemminig(tokensList)
    #tokensList = standadizedTextList
    #print(standardizedTextList)

    standadizedText = ''.join(tokensList)

    #tf_idf = calculateTf_idf_CosineSimilarity()
    #tfidf_matrix_train = tf_idf.calculateTf_idf(standadizedText)

    #similarityScore = tf_idf.calculateSimilarityScore(tfidf_matrix_train)
    #print(similarityScore)


