'''
Created on June 21, 2015

@authors: leiran biton, john o'brien
'''

from solver.solver import Solver, char_filter
from word import alphabetize
import requests
import re

class RulerSolver(Solver):
    '''
    The solver for the 6/21/2015 puzzle.
    '''
    pass

def get_rulers_list():
    pass

if __name__ == '__main__':
    p = """
Take the phrase "I am a monarch." Re-arrange the 
11 letters to name a world leader who was 
not a monarch but who ruled with similar authority. Who is it?
"""
    target = alphabetize("Iamamonarch".lower())
    # JO: Rulers.org looks good.
    # Trying wikipedia for though because I can easily iterate
    # using a numeric range.
    # page = requests.get('http://www.rulers.org/')

    for i in range(1900, 2015):
        print("Trying {0}".format(i))
        page = requests.get('https://en.wikipedia.org/wiki/List_of_state_leaders_in_{0}'.format(i))
        content = str(page.text.encode('ascii', 'ignore'))
        results = re.findall(r'title="(.*?)"', content)
        for result in results:
            temp = alphabetize(result.replace(" ", "").lower())
            if temp == target:
                print("Found: {0}->{1}".format(result, temp))
