'''
Created on May 19, 2015

@author: John.OBrien, Leiran.Biton
'''


from nltk.corpus import words, cmudict
from lazy import lazy



cmu = None


def nsyl(word):
    """Counts the number of syllables in a word.

    Keyword arguments:
    word -- a text string, which is intended to be a single word
    """
    # From http://www.onebloke.com/2011/06/counting-syllables-accurately-in-python-on-google-app-engine/    @IgnorePep8
    global cmu
    if cmu is None:
        cmu = cmudict.dict()  # @UndefinedVariable
    syllable_set = set()
    if word in cmu:
        for pronunciation in cmu[word]:
            syllable_count = 0
            for sound in pronunciation:
                if sound[-1].isdigit():
                    syllable_count += 1
            syllable_set.add(syllable_count)
    return syllable_set


def alphabetize(word):
    """Rearranges the letters in a word to place them in alphabetical order.

    Keyword arguments:
    word -- a text string, which is intended to be a single word
    """
    return("".join(sorted(word)).lower())


def build_anagrams(word_list):
    """

    The keys for "anagrams" are the alphabetized, lower cased
    version of a word. The value in each database entry is the set
    of all words which have the same alphabetized version, and are
    therefore anagrams of each other.
    """
    anagrams = {}
    for word in word_list:
        alpha = alphabetize(word)
        if alpha in anagrams:
            # We already have an anagram for this word
            # so add the current word to the set of anagrams
            anagrams[alpha].add(word)
        else:
            # We do NOT already have an anagram for this word
            # so let's create a new set object, starting with this word
            anagrams[alpha] = set([word])
    return anagrams

# build anagrams with full word list
anagrams = build_anagrams(words.words())

class Word(str):
    """
    Word class which set's a bunch of useful attributes.
    """

    def __init__(self, t):
        self.t = t
        self.anagrams = anagrams[alphabetize(self.t)]
        self.reversed = self.t[::-1]
        self.alphabetized = alphabetize(self.t)
        # Self.syllabes = a set where each element is a different pronounciations number of syllables
        # self.synonyms = list of synonyms
        # self.antonyms = list of antonyms
        super().__init__()

    @lazy
    def syllables(self):
        return nsyl(self.t)