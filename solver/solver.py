import sys
from time import sleep
import re
from nltk.corpus import words, wordnet, brown
import requests
import string

# a little easy to use lookup tool for on-the-fly use
def lookup(word):
    [print("{0}) {1}: {2}".format(i+1, a.name(), a.definition())) for i, a in enumerate(wordnet.synsets(word))]

def char_filter(text, chars="aeiouy", count=None):
    """
    Takes text input and a character filter (collection of characters) 
    to be removed from the text. Default filter = "aeiouy".
    Returns the original text input stripped of all of the characters in the filter.
    """
    result = text
    for letter in chars:
        if count == None:
            result = result.replace(letter, "")
        else:
            if result.replace(letter, "", count) == result:
                raise AssertionError("Character '{0}' is not in '{1}'.".format(letter, text))
            else:
                result = result.replace(letter, "", count)
    return result

def get_all_words():
    wordlist = set()
    lemmas = [lemma_name for lemma_name in wordnet.all_lemma_names()]
    print("lemmas:           ", len(lemmas))
    synsets = [syn.name()[:syn.name().index(".")] for syn in wordnet.all_synsets()]
    print("synsets:          ", len(synsets))
    corpus_words = words.words()
    print("words.words:      ", len(corpus_words))
    [wordlist.add(word) for word in lemmas + synsets + corpus_words]
    print("returned wordlist:", len(wordlist))
    return wordlist

class Solver(object):
    '''
    classdocs
    '''

    def __init__(self, puzzle_text, **kwargs):
        '''
        Constructor
        '''
        self.p = puzzle_text
        print("Puzzle:\n"+puzzle_text)
        self.candidates = set()
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def clear_candidates(self):
        """a method to clear the candidates list"""
        self.candidates = set()

    def get_words(self, kws):
        '''
        A method to create a set of words
        from the Wordnet corpus
        where any of a list of keywords are somewhere in the defintion.
        '''

        wordlist = set()
        allwords = get_all_words()
        for word in allwords:
            synset = wordnet.synsets(word)
            for syn in synset:
                if any([kw.lower() in syn.definition().lower() for kw in kws]):
                    wordlist.add(word)
                    wordlist.add(syn.name().split(".")[0].lower())
        return wordlist


def google_search(searchfor):
    '''
    Searches google
    using the requests library

    returns a requests.response object
    '''
    link = 'https://www.google.com/search?&q={0}'.format(searchfor)
    ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}
    payload = {'q': searchfor}
    response = requests.get(link, headers=ua, params=payload)
    t = response.text.encode(sys.stdout.encoding, errors='replace')
    # Add a five second sleep time to avoid google captcha's being triggered
    sleep(5)
    return str(t)


def ghits(searchfor):
    '''
    Searches google

    then parses the response to just
    return the approximate number of hits.
    '''
    content = google_search(searchfor)
    hits = re.search('id=\"resultStats\">About [0-9\,]* results', content)
    hits = int(char_filter(hits.group(), string.printable[10:])) # remove all except digits
    return hits


def search_brown(phrase):
    '''
    searches the brown corpus.

    phrase = list of words

    Returns of the number of times the phrase appears in the brown corpus.
    '''
    '''
    Might be able to leverage concordance to create a two word phrase
    concordance quick find index thing.

    emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
    emma.concordance("surprize")
    '''

    sentences = brown.sents()
    matches = 0
    for sentence in sentences:
        sentence = [word.lower() for word in sentence]
        for i in range(0, len(sentence) -1):
            frag = sentence[i:i + len(phrase)]
            if phrase == frag:
                matches += 1

    return matches
