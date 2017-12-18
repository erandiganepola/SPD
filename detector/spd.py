from Preprocessor.removingStopWords.RemovingStopWords import RemovingStopWords
from Preprocessor.replacingSynonyms.ReplacingSynonyms import ReplacingSynonyms
from Preprocessor.stemming.StemmingSinhala import StemmingSinhala
from Preprocessor.tokenizing.TokenizeText import TokenizeText
from Preprocessor.removingUnnecessaryChars.removeUnnecessaryChars import removeUnnecessaryChars


class SPD:
    @staticmethod
    def standardize(doc):
        text = doc
        print("Input: %r" % text)

        # TODO replace text between quotation marks by replacing with ""

        remove_unnecessary = removeUnnecessaryChars()
        text = remove_unnecessary.removePunctuation(text)
        print("Removed punctuations: %r" % text)

        text = remove_unnecessary.replaceNumbers(text)
        print("Numbers replaced: %r" % text)

        tokenizer = TokenizeText()
        tokens_list = tokenizer.tokenizeText(text)
        print("Tokens: %r" % tokens_list)

        stop_words_remover = RemovingStopWords()
        output = stop_words_remover.removeStopwords(tokens_list)
        tokens_list = output
        print("Removed stop words: %r" % output)

        replaced_synonyms = ReplacingSynonyms()
        synonyms_replaced_list = replaced_synonyms.replacingSynonyms(tokens_list)
        tokens_list = synonyms_replaced_list
        print("Synonym replaced: %r" % synonyms_replaced_list)

        print("Standardized Text: %r" % " ".join(tokens_list))

        stemming = StemmingSinhala()
        tokens_list = stemming.stem(tokens_list)
        print("Stemmed: %r" % tokens_list)

        standardized_text = " ".join(tokens_list);
        print("Standardized Text: %r" % standardized_text)
        return standardized_text

    @staticmethod
    def compare(doc1, doc2):
        return 0.01
