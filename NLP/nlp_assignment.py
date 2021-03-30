# create new text object with words with times they appear
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from pathlib import Path
import pandas as pd
from operator import itemgetter
from wordcloud import WordCloud
import imageio
import matplotlib.pyplot as plt

# READ BOOK OF JOHN IN
text = Path("book of John text.txt").read_text()

# function to test if something is a noun
is_noun = lambda pos: pos[:2] == "NN"
# do the nlp stuff
tokenized = nltk.word_tokenize(text)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

# IMPORT STOP WORDS AND FORM LIST OF THEM
stops = stopwords.words("english")
more_stops = [
    "thee",
    "thy",
    "thou",
    "ye",
    "therefore",
    "verily",
    "saith",
    "hath",
    "say",
    "art",
    "shall",
]
stops += more_stops

# TAKE OUT STOPS FROM LIST OF NOUNS
new_nouns = [x for x in nouns if x not in stops]
# print(new_nouns)

# CONVERT LIST TO STRING
textstr = ""
for i in new_nouns:
    textstr += i
    textstr += " "

# CONVERT TO TEXTBLOB TO ANALYZE
blob = TextBlob(textstr)
items = blob.word_counts.items()

# SORT THE LIST SO THAT THE HIGHEST REPEATED WORDS COME FIRST
sorted_items = sorted(items, key=itemgetter(1), reverse=True)
top15 = sorted_items[:15]

# MAKE STRING OUT OF TOP 15
top15str = ""
first_tuple_elements = [a[0] for a in top15]
for i in first_tuple_elements:
    top15str += i
    top15str += " "
print(top15str)

# MAKE WORDCLOUD
wordcloud = WordCloud(colormap="Blues", background_color="gray")
wordcloud = wordcloud.generate(top15str)
wordcloud = wordcloud.to_file("BookOfJohn.png")
plt.imshow(wordcloud)
print("done")
