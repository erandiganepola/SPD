import re


class removeUnnecessaryChars():
    def removeChars(self, text):
        cyril = re.compile(u'[\u0021-\u007F]', re.UNICODE)

        plaiText = cyril.sub('', str(text))

        return plaiText
