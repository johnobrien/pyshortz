'''
Created on May 24, 2015

@author: johno_000
'''


from solver.solver import Solver
from solver.word import alphabetize
import csv


class MySolver(Solver):
    '''
    MySolver is an example solver
    which is a child of the solver class.
    '''
    
    def solve_with_nltk(self, kws):
        '''
        Solving the puzzle for this week using nltk.
        '''
        print("accessing nltk with keyword list:")
        for keyword in kws:
            print("    {0}".format(keyword))
        wordnet_jobs = self.get_words(kws)
        print("retrieved {0} potential entries".format(len(wordnet_jobs)))
        self.try_list("wordnet", wordnet_jobs)

    def solve_with_csv(self, filename):
        '''
        Solving the puzzle for this week using a preloaded file of jobs.
        '''
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            csv_jobs = list(reader)
            print("retrieved {0} potential entries".format(len(csv_jobs)))
            self.try_list("User supplied job list", csv_jobs)

    def solve_with_both(self, filename, kws):
        '''
        Solving the puzzle for this week using both a preloaded file of jobs and nltk
        '''
        print("accessing nltk with keyword list:")
        for keyword in kws:
            print("    {0}".format(keyword))
        wordnet_jobs = self.get_words(kws)
        print("retrieved {0} potential entries".format(len(wordnet_jobs)))
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            csv_jobs = list(reader)
            print("retrieved {0} potential entries".format(len(csv_jobs)))
            self.try_list("both lists", list(wordnet_jobs) + csv_jobs)
        
    def try_list(self, list_name, jobs):
        '''
        Takes a list job titles,
        and trys to find whether any of them together
        match merchant raider alphabetized.
        '''
        print("generating anagrams")
        anagrams = dict()
        alpha_list = [alphabetize(job) for job in jobs]
        for job1 in jobs:
            remaining_letters = self.word
            for letter in job1:
                try:
                    letter_index = remaining_letters.index(letter)
                except ValueError:
                    break
                    remaining_letters = remaining_letters[:letter_index] \
                                      + remaining_letters[letter_index+1:]
            if alphabetize(remaining_letters) in alpha_list:
                job2 = jobs[alpha_list.index(alphabetize(remaining_letters))]
                anagrams[alphabetize(job1+job2)] = [job1, job2]
        try:
            print("Jobs are {0} and {1}".format(anagrams[self.word.alphebatized][0],
                                                anagrams[self.word.alphebatized][1]))
        except:
            print("{0} list do not find a match.".format(list_name))

        return
        

if __name__ == '__main__':

    kws = ["occupation",
           "job",
           "someone",
           "person",
           "a man",
           "a woman",
           "duty",
           "duties" ,
           "officer" ,
           "exuctive" ,
           "operator" ,
           "employee" ,
           "who" ,
           "official" ,
           "writer" ,
           "a female" 
           ]

    p = '''Take the phrase "merchant raider." A merchant raider was a vessel in
World War I and World War II that targeted enemy merchant ships. Rearrange the
letters of "merchant raider" to get two well-known professions. What are
they?'''

    s = MySolver(p, word="merchantraider")
    #s.solve_with_nltk(kws)
    #s.solve_with_csv('jobs.csv')
    s.solve_with_both("jobs.csv", kws)
