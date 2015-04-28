#!/usr/local/bin/env python
'''
Created on Apr 26, 2015

@authors: Leiran Biton, John O'Brien
'''
"""solution to the 4-26-2015 NPR puzzle for pyshortz blog."""

problem = """Problem:
Name a famous actor whose first and last names both are 
seven letters long. Change the first three letters of 
the actor's last name to three new letters and you'll 
name another famous actor. They share the same first 
name. Add the three letters you changed in the first 
actor's last name plus the three letters you changed 
to get the second actor's name, and you'll spell the 
last name of a third famous actor. 

Who are these three Hollywood stars?
"""

import requests
import re

class Solution(object):
    '''
    Solution object
    
    '''
    def first_actor(self, actor):
        '''
        Checks to see whether a string meets
        the requirements to be the first actor
        
        Args:
            actor (str): the name of a famous actor where the first and last name
                        are both seven letters long
        Returns:
            True if the requirements are met, False if they are not


        '''
        first, last = actor.split()
        return len(first) == 7 and len(last) == 7
        

    def second_actor(self, actor1, actor2):
        '''
        Checks to see whether given the first actor
        a string meets the requirements to be the 
        second actor
        
        
        Args:
            actor1 (str): the name of a famous actor where the first and last name
                        are both seven letters long
            actor2 (str): the name of the famous actor who shares the same first name
                        as actor 1, and for whom the rest of his last name, excluding the
                        first three letters, matches actor1
        Returns:
            True if the requirements are met, False if they are not
            
        '''
        first1, last1 = actor1.split()
        first2, last2 = actor2.split()

        if actor1 == actor2: return False
        
        return first1.lower() == first2.lower() and \
            last1[3:].lower() == last2[3:].lower()

    def third_actor(self, actor1, actor2, actor3):
        '''
        Checks to see whether given the first and second actors
        a string meets the requirements to be the third actor
        
        
        Args:
            actor1 (str): the name of a famous actor where the first and last name
                        are both seven letters long
            actor2 (str): the name of the famous actor who shares the same first name
                        as actor 1, and for whom the rest of his last name, excluding the
                        first three letters, matches actor1
            actor (str): the name of a famous actor whose last name is comprised of the first
                        three letters of the actor1's last name combined with the first three letters
                        of the actor2's last name
        Returns:
            True if the requirements are met, False if they are not
            
        '''
        first1, last1 = actor1.split()
        first2, last2 = actor2.split()
        first3, last3 = actor3.split()
 
        return last3.lower() == (last1[:3] + last2[:3]).lower()

    def process_actors(self, actors):
        '''
        Searches a set of actors to find three that meet the requirements
        
        Args:
            actors (set): a set of actors names, each of which is two words long
        Returns:
            possible_answers (set): a set of tuples, each of which is comprised
                                    of three strings of the names of three actors who
                                    meet the requirements
            
        '''
        possible_answers  = set()
        actors1 = []
        
        if self.verbose: print("Processing names for eligibility as the first actor...")
        for actor1 in actors:
            if self.first_actor(actor1): 
                actors1.append(actor1)
        
        if self.verbose: print("Processing names for eligibility as the second actor...")
        for actor2 in actors:
            for actor1 in actors1:
                if self.second_actor(actor1, actor2): 
                    for actor3 in actors:
                        if self.third_actor(actor1, actor2, actor3):
                            possible_answers.add((actor1, actor2, actor3))


        return possible_answers

    def __init__(self, actors, verbose=False):
        '''
        Args:
            actor (set): A list of strings, each of which is the first and last name of an actor
                    
        Example self.possible_answers value:
            possible_answers = {("Earnest Fleming",
                                 "Earnest Troming",
                                 "Killing Fletro")}
            
        '''
        self.verbose = verbose
        if actors:
            self.possible_answers = self.process_actors(actors)

if __name__ == "__main__":
    print("\n"+problem)
    # From http://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Stars
    # Maybe try to scrape movie star names from http://projects.latimes.com/hollywood/star-walk/list/
    
    actors = []
    page = requests.get('http://projects.latimes.com/hollywood/star-walk/list/')
    urls = re.findall(r'<a href="/hollywood/star-walk/.*</a>', page.text)
    for url in urls:
        t = re.findall('>.*<', url)
        actor = t[0]
        actor = actor[1:-1]
        if actor.count(" ") == 1 and actor.count(",") == 1:
            last, first = actor.split(",")
            actors.append(first + " " + last)
    
    s = Solution(actors, verbose=True)
    print("Candidates:")
    if s.possible_answers:
        for actor1, actor2, actor3 in s.possible_answers:
            print("{0}, {1} -> {2}".format(actor1, actor2, actor3))
    else:
        print("\n No possible answers were found.")
