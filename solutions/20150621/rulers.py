'''
Created on June 21, 2015

@authors: leiran biton, john o'brien
'''

from string import ascii_lowercase, punctuation
from nltk.corpus import wordnet
from solver.solver import Solver, get_all_words, char_filter
from lxml import html
import requests

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
    # From http://docs.python-guide.org/en/latest/scenarios/scrape/
    # JO: Leiran, is this a list of real leaders or leaders in a video game?
    page = requests.get('http://www.eu4wiki.com/List_of_rulers')
    tree = html.fromstring(page.text)
    # From http://stackoverflow.com/questions/6325216/parse-html-table-to-python-list
    # TODO: Magic goes here that uses xpath to get a table out of HTML.
    table = tree.MAGIC
    rows = iter(table)
    headers = [col.text for col in next(rows)]
    for row in rows:
        values = [col.text for col in row]
        print dict(zip(headers, values))
