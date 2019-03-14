import nltk
from nltk.corpus import stopwords

def parser(zdanie):
     stop_words = set(stopwords.words('english'))
     stop_words.remove("not")
     words = nltk.word_tokenize(zdanie)
     filtered = [w for w in words if w not in stop_words]
     #tagged = nltk.pos_tag(words, lang='eng')
     #chunkGram = r"""Context: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
     #chunkParser = nltk.RegexpParser(chunkGram)
     #chunked = chunkParser.parse(tagged)
     return " ".join(filtered)


test="Please leave your footwear outside. " \
     "Will you wait here? " \
     "Where have you been all this while? " \
     "We will not tolerate this. " \
     "I am your friend." \
     " My sister lives in Mexico. " \
     "What did you do then? " \
     "Do be a bit more careful. " \
     "Never speak to me like that again. " \
     "Always remember what I told you.  " \
     "The ball rolled slowly into the goal."


zdania = nltk.sent_tokenize(test)
for i in zdania:
     print(parser(i))


