
import re
import statistics
from textstat import flesch_reading_ease, lexicon_count
import string
import re
from collections import Counter
from spellchecker import SpellChecker

# Define Functions to extract features from given data set.add

# 1 Lenght Variance
def length_variance(X):
    return [[
        statistics.variance(lengths) if len(lengths) > 1 else 0
    ] for x in X.ravel()
      for lengths in [[len(s.split()) for s in re.split(r'[;.!?]', x) if s.strip()]]
    ]

# 2 Readiability Score
def readability_score(X):
    return [[flesch_reading_ease(x)] for x in X.ravel()]

# 3 Remove punctuatins
def remove_punctuation(X):
    return [[len(x.translate(str.maketrans('', '', string.punctuation)).split())] for x in X.ravel()]

# 4 Repeatition Score
def repetition_score(X):
    return [[
        sum(1 for count in Counter(x.split()).values() if count > 1) / len(x.split()) * 100
    ] for x in X.ravel()]

# 5 Creativity Score
def creativity_score(X):
    return [[
        len(set(x.split())) / len(x.split()) * 100
    ] for x in X.ravel()]

# 6 Typo Mistake Count in percentage
def typo_count(X):
    spell = SpellChecker()
    return [[
        (len(spell.unknown(x.split())) / len(x.split())) * 100 if len(x.split()) > 0 else 0
    ] for x in X.ravel()]

###############################################################################################

# Reason Finding Functions

# Length Variancce 
def p_lenght_variance(text):
    sentences = re.split(r'[;.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    lengths = [len(sentence.split()) for sentence in sentences]
    variance = statistics.variance(lengths) if len(lengths) > 1 else 0
    return variance

# readiability score
def p_readability_score(text):
    return flesch_reading_ease(text)

# Removing Punctuations
def p_remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))


# Repeatition_score
def p_repetition_score(text):
    words = text.split(' ')
    counter = Counter(words)
    repeated = [1 for word, count in counter.items() if count > 1]
    return sum(repeated) / len(words) * 100

# creativity_score human ---> high creativity_score
def p_creativity_score(text):
    words = text.split()
    unique = len(set(words))
    return unique / len(words) * 100


# typo count
def p_typo_count(text):
    spell = SpellChecker()
    words = text.split()
    misspelled = spell.unknown(words)
    return (len(misspelled) / len(words)) * 100


