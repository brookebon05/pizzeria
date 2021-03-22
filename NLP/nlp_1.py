from textblob import TextBlob
from textblob import Word

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
# print(index.pluralize()) #prints indices

cacti = Word("cacti")
# print(cacti.singularize())
animals = TextBlob("dog cat fish bird").words

# print(animals.pluralize())

# word = Word("theyr")
# print(word.spellcheck())
# word.correct()
# print(word)

sentence = TextBlob("Ths sentence has missplled words")
corr_sentence = sentence.correct()
# print(corr_sentence)

# lemmatization: varieties to variety

word1 = Word("studies")
word2 = Word("varieties")
print(word1.lemmatize())  # prints study

happy = Word("happy")
print(happy.definitions)  # prints definitions of happy
"""
for synset in happy.synsets:
    print(synset)  # every synset has a lemma
    print(lemma)
    print(lemma.name())  # gives us synonyms
"""
lemmas = happy.synsets[0].lemmas()
print(lemmas)
for lemma in lemmas[0].antonyms():
    print(lemma.name())

import nltk

# nltk.download("stopwords")
from nltk.corpus import stopwords

stops = stopwords.words("english")

print(stops)

text = "Today is a beautiful day."
blob = TextBlob(text)
# eliminate words using list comprehension
# blob.words will be a list
newlist = [i for i in blob.words if word not in stops]
print(newlist)
