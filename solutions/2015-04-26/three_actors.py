#!/usr/local/bin/env python
'''
Created on Apr 26, 2015

@authors: Leiran Biton, John O'Brien
'''
"""solution to the 4-19-2015 NPR puzzle for pyshortz blog."""

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
        if actors:
        
            for actor1 in actors:
                for actor2 in actors:
                    for actor3 in actors:
                        if self.first_actor(actor1) and \
                           self.second_actor(actor1, actor2) and \
                           self.third_actor(actor1, actor2, actor3):
                            possible_answers.add((actor1, actor2, actor3))

        return possible_answers


    def __init__(self, actors):
        '''
        Args:
            actor (set): A list of strings, each of which is the first and last name of an actor
                    
        Example self.possible_answers value:
            possible_answers = {("Earnest Fleming",
                                 "Earnest Troming",
                                 "Killing Fletr")}
            
        '''
        self.possible_answers = self.process_actors(actors)

if __name__ == "__main__":
    print("\n"+problem)
    actors = {  'Humphrey Bogart',
                'Cary Grant',
                'James Stewart',
                'Marlon Brando',
                'Fred Astaire',
                'Henry Fonda',
                'Clark Gable',
                'James Cagney',
                'Spencer Tracy',
                'Charlie Chaplin',
                'Gary Cooper',
                'Gregory Peck',
                'John Wayne',
                'Laurence Olivier',
                'Gene Kelly',
                'Orson Welles',
                'Kirk Douglas',
                'James Dean',
                'Burt Lancaster',
                'Marx Brothers',
                'Buster Keaton',
                'Sidney Poitier',
                'Robert Mitchum',
                'Edward Robinson',
                'William Holden',
                'Katharine Hepburn',
                'Bette Davis',
                'Audrey Hepburn',
                'Ingrid Bergman',
                'Greta Garbo',
                'Marilyn Monroe',
                'Elizabeth Taylor',
                'Judy Garland',
                'Marlene Dietrich',
                'Joan Crawford',
                'Barbara Stanwyck',
                'Claudette Colbert',
                'Grace Kelly',
                'Ginger Rogers',
                'Mae West',
                'Vivien Leigh',
                'Lillian Gish',
                'Shirley Temple',
                'Rita Hayworth',
                'Lauren Bacall',
                'Sophia Loren',
                'Jean Harlow',
                'Carole Lombard',
                'Mary Pickford',
                'Ava Gardner',
                }

    s = Solution(actors)
    if s.possible_answers:
        for possible_answer in s.possible_answers:
            print(possible_answer)
    else:
        print("No possible answers were found.")