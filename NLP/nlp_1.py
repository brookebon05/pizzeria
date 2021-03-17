from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."
blob = TextBlob(text)  # converts text into blob
"""
print(blob)
print(blob.sentences)
print(blob.words)  # creates list
print(blob.tags)
print(blob.noun_phrases)  # includes adjectives
print(blob.sentiment)

print(round(blob.sentiment.polarity), 2)
print(round(blob.sentiment.subjectivity), 3)

sentences = blob.sentences
for sentence in sentences:
    print(sentence)
    print(sentence)
    print(round(sentence.sentiment.polarity, 3))

from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(
    text, analyzer=NaiveBayesAnalyzer()
)  # gives positivity and negativity factors
"""
# print(blob.sentiment)

# print(blob.detect_language())
# spanish = blob.translate(to="es")
# print(spanish)

from textblob import Word

index = Word("index")
print(index.pluralize())

cacti = Word("cacti")
print(cacti.singularize())
animals = TextBlob("dog cat fish bird").words

print(animals.pluralize())

word = Word("theyr")
print(word.spellcheck())
word.correct()
print(word)

sentence = TextBlob("Ths sentence has missplled words")
corr_sentence = sentence.correct()
print(corr_sentence)
