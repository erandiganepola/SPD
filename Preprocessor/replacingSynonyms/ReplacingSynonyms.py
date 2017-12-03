import io


class ReplacingSynonyms:
    def replacingSynonyms(self, tokensList):
        synonymList = [line.split(",") for line in
                       io.open('Test/sample_synonyms.txt', 'r', encoding='utf-16').read().splitlines()]

        for index, token in enumerate(tokensList):
            for synonyms in synonymList:
                if token in synonyms:
                    tokensList[index] = synonyms[0]
                    break
        return tokensList
