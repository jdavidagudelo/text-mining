import nltk
nltk.download()

from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist

FreqDist()
import nltk
from nltk.corpus import inaugural
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target))

data = cfd['america']

nltk.re_show()