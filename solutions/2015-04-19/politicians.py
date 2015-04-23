#!/usr/local/bin/env python
"""solution to the 4-19-2015 NPR puzzle for pyshortz blog."""

problem = """Problem:
Take the first names of two politicians in the news. 
Switch the first letters of their names and read the
result backward to name something that each of these 
politicians is not.
"""

class solution:
    
    def switch_letters(self, name1, name2):     
        "input two names. returns those names with their first letters switched."
        return (name2[0]+name1[1:]).lower(), (name1[0]+name2[1:]).lower()

    def read_backward(self, name):
        "returns the string input, backward."
        return name[::-1]

    def process_names(self, name1, name2):
        "process the names through switch_letters and read_backward"
        temp_word1, temp_word2 = [name for name in \
                        self.switch_letters(name1, name2)]
        
        word1 = self.read_backward(temp_word1 + temp_word2)
        word2 = self.read_backward(temp_word2 + temp_word1)
        
        for word in word1, word2:
            if word in self.match_against:
                # comes back if it gets a hit on the first
                # even if the second could be a hit too
                # but whatever for now...
                return word
            else:
                return None
    
    def __init__(self, names):
        from nltk.corpus import words, wordnet
        self.wordnet = wordnet
        self.match_against = words.words()
        self.candidates = []
        for i, name1 in enumerate(names):
            for j, name2 in enumerate(names):
                if i < j:
                    if self.process_names(name1, name2):
                        word = self.process_names(name1, name2)
                        self.candidates.append((name1, name2, word))
        
if __name__ == "__main__":
    print("\n"+problem)
    print("Run test_politicians to run tests.")
#     # hand-made list
#     # from http://thehill.com/homenews/campaign/215523-the-65-people-who-may-run-for-president-in-2016
 
    presidential_candidates = {  "Joe",
                                 "Joseph",
                                 "Jerry",
                                 "Hillary",
                                 "Andrew",
                                 "Russ",
                                 "Al",
                                 "Maggie",
                                 "Margaret",
                                 "John",
                                 "Amy",
                                 "Martin",
                                 "Janet",
                                 "Jay",
                                 "Deval",
                                 "Bernie",
                                 "Brian",
                                 "Mark",
                                 "Elizabeth",
                                 "Jim",
                                 "Kelly",
                                 "Michele",
                                 "Haley",
                                 "Marsha",
                                 "John",
                                 "Scott",
                                 "Jeb",
                                 "Herman",
                                 "Ben",
                                 "Chris",
                                 "Ted",
                                 "Mitch",
                                 "Mary",
                                 "Bill",
                                 "William",
                                 "Newt",
                                 "Nikki",
                                 "Mike",
                                 "Bobby",
                                 "Robert",
                                 "Pete",
                                 "Peter",
                                 "Steve",
                                 "Steven",
                                 "Susana",
                                 "Cathy",
                                 "Sarah",
                                 "Rand",
                                 "Mike",
                                 "Rick",
                                 "Condoleezza",
                                 "Mike",
                                 "Michael",
                                 "Mitt",
                                 "Marco",
                                 "Paul",
                                 "Brian",
                                 "Rick",
                                 "Joe",
                                 "Joseph",
                                 "Tim",
                                 "Donald",
                                 "Don",
                                 "Scott",
                                 "Allen"}
    print("Add names from file pols.txt to list of presidential candidates...")

    with open("pols.txt", "r") as f:
        names = set([name.split()[0] for name in f.readlines()])
    
    # Leiran, I think you can just use the update method of a set and
    # only the unique items are added.
    names.update(presidential_candidates)
    s = solution(names)
    if len(s.candidates):
        for n, candidate in enumerate(s.candidates):
            print("{0}. Answer could be:{1},{2}-->{3}".format(n, candidate[0], candidate[1], candidate[2]))
    else:
        print("There were no possible answers generated by the hand-crafted list.")
    print("Done.")
