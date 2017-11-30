import io
import os


class StemmingSinhala():
    def stemminig(self, tokensList):

        suffFileDirec = os.path.dirname(os.path.abspath(__file__)) + "/../resources/suffix.txt"
        try:
            suffixFile = io.open(suffFileDirec, "r", encoding='utf-16').read()
        except UnicodeDecodeError:
            suffixFile = io.open(suffFileDirec, "r", encoding='latin-1').read()

        suffixList = suffixFile.split()

        tokensList.sort()
        wordList = tokensList

        i = 0
        j = 0
        while (i < len(wordList)):

            while (j < len(wordList)):

                benchWord = suffixList[i]  # 0
                checkWord = wordList[j]  # 1

                for suffix in suffixList:
                    if checkWord[j].endswith(suffix):
                        wordList[j] = benchWord
                        break
            j += 1

        i += 1

        return wordList
