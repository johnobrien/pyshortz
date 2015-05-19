#!/usr/local/bin/python
'''
Created on May 18, 2015

Solver for the May 17, 2015 NPR Sunday Puzzle

@author: Leiran Biton
'''
# imports
import pycountry
from solver.solver import Solver, char_filter
from string import punctuation

p = \
"""Name a country with at least three consonants. 
These are the same consonants, in the same order, 
as in the name of a language spoken by millions 
of people worldwide. The country and the place 
where the language is principally spoken are in 
different parts of the globe. 

What country and what language are these?"""

class MySolver(Solver):
    '''
    MySolver is an example solver
    which is a child of the solver class.
    '''
    
    # set methods
    char_filter=char_filter
    
    # set attributes
    country_names  = [country.name  for country  in pycountry.countries]
    # remove commas and parentheticals, add parentheticals as additional country names
    for c, country_name in enumerate(country_names):
        if "," in country_name:
            country_names[c] = country_name[:country_name.index(",")]
        if "(" in country_name:
            begin_parens = country_name.index("(")
            end_parens   = country_name.index(")")
            country_names.append(country_name[begin_parens+1:end_parens])
            country_names[c] = country_name[:begin_parens]+country_name[end_parens+1:]
    language_names = [language.name for language in pycountry.languages]
    
    countries_no_vowels      = [char_filter(country.lower(), "aeiou "+punctuation)  for country in country_names]
    countries_no_vowels_no_y = [char_filter(country.lower(), "aeiouy "+punctuation) for country in country_names]
    
    languages_no_vowels      = [char_filter(lang.lower(), "aeiou "+punctuation)  for lang in language_names]
    languages_no_vowels_no_y = [char_filter(lang.lower(), "aeiouy "+punctuation) for lang in language_names]
    
    def solve(self):
        '''
        the main new method
        which I figure each MySolver
        will create,
        which solves the particular problem
        for each particular week.
        '''
        for c, country in enumerate(self.country_names):
            for country_list, language_list in ((self.countries_no_vowels, self.languages_no_vowels)
                                               ,(self.countries_no_vowels_no_y, self.languages_no_vowels_no_y)
                                               ,(self.countries_no_vowels, self.languages_no_vowels_no_y)
                                               ,(self.countries_no_vowels_no_y, self.languages_no_vowels)
                                               ):
                if country_list[c] in language_list and len(country_list[c])>=3:
                    lang_index = language_list.index(country_list[c])
                    self.candidates.add((country, self.language_names[lang_index]))
        
        return self.candidates

if __name__ == '__main__':
    s = MySolver(p)
    s.solve()
    if s.candidates:
        print("Candidates:")
        for candidate in s.candidates:
            print("    Country: {0}, Language: {1}".format(*candidate))
    else:
        print("No candidates were found.")
