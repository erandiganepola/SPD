import io

import Preprocessor


class ReplacingSynonyms:
    def replacingSynonyms(self, tokensList):
        path = Preprocessor.__file__
        path = path.replace("__init__.py", "resources/sample_synonyms.txt")

        synonym_list = [line.split(",") for line in io.open(path, 'r', encoding='utf-16').read().splitlines()]

        for index, token in enumerate(tokensList):
            for synonyms in synonym_list:
                if token in synonyms:
                    tokensList[index] = synonyms[0]
                    break
        return tokensList
