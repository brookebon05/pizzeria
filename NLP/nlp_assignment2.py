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
blob = TextBlob(text)

# MAKE STOPS LIST
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

# MAKE LIST OF ITEMS NOT IN STOPS
items = blob.noun_phrases
items = [item for item in items if item not in stops]

# SORT THESE ITEMS
sorted_items = sorted(items)
sorted_items = sorted(items, key=itemgetter(1), reverse=True)
top15 = sorted_items[:15]
print(top15)