from nltk.tokenize import word_tokenize


class TokenizeText:
    def tokenizeText(self, text):
        tokenArray = []
        tokens = word_tokenize(text)

        for i in tokens:
            tokenArray.append(i)
        return tokenArray
