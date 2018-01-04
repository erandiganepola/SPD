import io

from Preprocessor.QuoteRemover import QuoteRemover

txt = io.open("/home/imesha/Desktop/para1.txt").read()
print(txt)
txt = QuoteRemover.remove_quotes(txt)
print(txt)
