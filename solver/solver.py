
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

    def __init__(self, puzzle_text):
        '''
        Constructor
        '''
        self.p = puzzle_text
        print("Puzzle:\n"+puzzle_text)
        self.candidates = set()

    def dummy_method(self):
        '''
        To test that my import is working.
        '''
        return "It's working!"
