import io


class StemmingSinhala():
    def stem(self, tokens_list):
        try:
            suffix_list = io.open("Preprocessor/resources/suffixes.txt", "r", encoding='utf-8').read().splitlines()
        except UnicodeDecodeError:
            suffix_list = io.open("Preprocessor/resources/suffixes.txt", "r", encoding='latin-1').read().splitlines()

        stemmed = []
        for token in tokens_list:
            word = token
            for suffix in suffix_list:
                if word.endswith(suffix):
                    word = word.replace(suffix, "")
            stemmed.append(word)

        return stemmed
