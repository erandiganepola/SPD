import io
import os


class StemmingSinhala():
    def stemminig(self, doc):

        doc1 = doc

        suffFileDirec = os.path.dirname(os.path.abspath(__file__)) + "/../resources/suffixes.txt"
        try:
            suffixFile = io.open(suffFileDirec, "r", encoding='utf-8').read()
        except UnicodeDecodeError:
            suffixFile = io.open(suffFileDirec, "r", encoding='latin-1').read()

        suffixList = suffixFile.split()

        doc.sort()
        wordList = doc

        i = 0
        while (i < len(wordList) - 1):
            j = i + 1

            while (j < len(wordList)):

                benchWord = wordList[i]
                checkWord = wordList[j]
                benchCharList = list(benchWord)
                checkCharList = list(checkWord)

                if (checkWord.startswith(benchWord)):
                    for suffix in suffixList:
                        if checkWord.endswith(suffix):
                            wordList[j] = benchWord
                            break
                j += 1
            i += 1
