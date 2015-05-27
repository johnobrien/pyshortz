from nltk.corpus import words, wordnet


def char_filter(text, chars="aeiouy", count=None):
    """
    Takes text input and a character filter (collection of characters) 
    to be removed from the text. Default filter = "aeiouy".
    Returns the original text input stripped of all of the characters in the filter.
    """
    if count == None:
        return text.replace(chars, "") \
            if len(chars) == 1 \
            else char_filter(text.replace(chars[0], ""), chars[1:])
    else:
        return text.replace(chars, "", count) \
            if len(chars) == 1 \
            else char_filter(text.replace(chars[0], "", count), chars[1:])

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
        for word in words.words():
            synset = wordnet.synsets(word)
            for syn in synset:
                if any([kw.lower() in syn.definition().lower() for kw in kws]):
                    wordlist.add(syn.name().split(".")[0].lower())

        return wordlist

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