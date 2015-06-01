import sys
from time import sleep
import re
from nltk.corpus import words, wordnet
import requests

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


def googlesearch(searchfor):                                                                                                                                                                                       
    '''
    Searches google
    using the requests library
    
    returns a requests.response object
    '''
    link = 'http://www.google.com/search?q={0}'.format(searchfor)                                                                                                                              
    ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}                                                                
    payload = {'q': searchfor}                                                                                                                                                                                     
    response = requests.get(link, headers=ua, params=payload)                                                                                                                                                      
    t = response.text.encode(sys.stdout.encoding, errors='replace')
    # Add a one second sleep time to avoid google captcha's being triggered
    sleep(1)
    return str(t)


def ghits(searchfor):
    '''
    Searches google

    then parses the response to just
    return the approximate number of hits.
    '''
    content = googlesearch(searchfor)
    print(content)
    regex = re.compile('id=\"resultStats\">About .* results')
    hits = regex.match(content)
    hits = int(hits.replace(',', ''))
    return hits


if __name__ == "__main__":
    import unittest
    #from solver import Solver, char_filter
    
    vowels = "aeiou"
    class TestWord(unittest.TestCase):
        def test_vowels(self):
            self.assertEqual(char_filter("christmas", vowels), "chrstms")
        def test_butterfly(self):
            self.assertEqual(char_filter("butterfly", "t"), "buerfly")
        def test_single_filter(self):
            self.assertEqual(char_filter("butterstick", "t", 1), "buterstick")
            self.assertEqual(char_filter("butterstick", "t", 2), "buerstick")
            self.assertEqual(char_filter("butterstick", "t", 3), "buersick")
        def test_multiple_filter(self):
            self.assertEqual(char_filter("mississippi", "is"), "mpp")
            self.assertEqual(char_filter("mississippi", "is", 1), "msissippi")
            self.assertEqual(char_filter("mississippi", "is", 2), "mssippi")
            self.assertEqual(char_filter("mississippi", "is", 3), "msppi")
        def test_count(self):
            self.assertEqual(char_filter("basement", vowels, 1), "bsment")
    
    unittest.main()