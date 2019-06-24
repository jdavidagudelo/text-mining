import nltk
from nltk.corpus import brown
from bs4 import BeautifulSoup

from nltk import Prover9

def count_words_by_genre():
    cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in brown.categories()
        for word in brown.words(categories=genre))
    return cfd


def conditional_freq_dist():
    from nltk.corpus import udhr
    languages = ['Chickasaw', 'English', 'German_Deutsch',
                 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
    cfd = nltk.ConditionalFreqDist(
        (lang, len(word))
        for lang in languages
        for word in udhr.words(lang + '-Latin1'))
    cfd.tabulate(conditions=['English', 'German_Deutsch'], samples=range(10), cumulative=True)


def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()
    print()

