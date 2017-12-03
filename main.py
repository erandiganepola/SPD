import io

from Preprocessor.removingStopWords.RemovingStopWords import RemovingStopWords
from Preprocessor.stemming.StemmingSinhala import StemmingSinhala
from Preprocessor.creatingN_Grams.CreateN_Grams import CreateN_Grams
from Preprocessor.tokenizing.TokenizeText import TokenizeText
from Preprocessor.replacingSynonyms.ReplacingSynonyms import ReplacingSynonyms
# from SimilarityComparissor.calculateTf_idf_CosineSimilarity import calculateTf_idf_CosineSimilarity

from Preprocessor.removingUnnecessaryChars.removeUnnecessaryChars import removeUnnecessaryChars

if __name__ == '__main__':
    text = io.open('Test/para1.txt', 'r', encoding='utf-16').read()
    print("Input: %r\n" % text)

    # TODO replace text between quotation marks by replacing with ""

    removeUnnecessary = removeUnnecessaryChars()
    text = removeUnnecessary.removePunctuation(text)
    print("Removed punctuations: %r\n" % text)

    text = removeUnnecessary.replaceNumbers(text)
    print("Numbers replaced: %r\n" % text)

    tokenizer = TokenizeText()
    tokensList = tokenizer.tokenizeText(text)
    print("Tokens: %r\n" % tokensList)

    stopWordsRemover = RemovingStopWords()
    output = stopWordsRemover.removeStopwords(tokensList)
    tokensList = output
    print("Removed stop words: %r\n" % output)

    replacedSynonyms = ReplacingSynonyms()
    synonymsReplacedList = replacedSynonyms.replacingSynonyms(tokensList)
    tokensList = synonymsReplacedList
    print("Synonym replaced: %r\n" % synonymsReplacedList)

    nGramCreator = CreateN_Grams()
    nGrams = nGramCreator.createN_Grams(tokensList, 3)
    print("N-Grams: %r\n" % nGrams)

    # stemming = StemmingSinhala()
    # standardizedTextList = stemming.stemminig(tokensList)
    # tokensList = standadizedTextList
    # print(standardizedTextList)

    standadizedText = ' '.join(tokensList)
    print("Standardized Text: %r\n" % standadizedText)

    # tf_idf = calculateTf_idf_CosineSimilarity()
    # tfidf_matrix_train = tf_idf.calculateTf_idf(standadizedText)

    # similarityScore = tf_idf.calculateSimilarityScore(tfidf_matrix_train)
    # print(similarityScore)
