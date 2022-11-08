import re
import string
import pymorphy2

STOPWORDS = {'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i', 'it', 'for', 'not', 'on', 'with', 'he',
             'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'wikipedia'}
PUNCTUATION = re.compile('[%s]' % re.escape(string.punctuation))
morph = pymorphy2.MorphAnalyzer()


def tokenize(text):
    return text.split()


def lowercase_filter(tokens):
    return [token.lower() for token in tokens]


def punctuation_filter(tokens):
    return [PUNCTUATION.sub('', token) for token in tokens]


def stopword_filter(tokens):
    return [token for token in tokens if token not in STOPWORDS]


def lemmatize(tokens):
    words = tokens  # разбиваем текст на слова
    res = list()
    for word in words:
        p = morph.parse(word)[0]
        res.append(p.normal_form)

    return res


def analyze(text):
    tokens = tokenize(text)
    tokens = lowercase_filter(tokens)
    tokens = punctuation_filter(tokens)
    tokens = stopword_filter(tokens)
    tokens = lemmatize(tokens)

    return {token for token in tokens if token}