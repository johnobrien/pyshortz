from nltk.corpus import words, wordnet


def char_filter(text, chars="aeiouy"):
    """
    Takes text input and a character filter (collection of characters) 
    to be removed from the text. Default filter = "aeiouy".
    Returns the original text input stripped of all of the characters in the filter.
    """
    return text.replace(chars[0], "") \
        if len(chars) == 1 \
        else char_filter(text.replace(chars[0], ""), chars[1:])

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

    def get_words(self, kws):
        '''
        A method to create a set of words
        from the Wordnet corpus
        where any of a list of keywords are somewhere in the defintion.
        '''

        wordlist = set()
        for word in words.words():
            synset = wordnet.synsets(word)
            for syn in synset:
                if any([kw.lower() in syn.definition().lower() for kw in kws]):
                    wordlist.add(syn.name().split(".")[0].lower())

        return wordlist
