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
        word1, word2 = [self.read_backward(name) for name in \
                        self.switch_letters(name1, name2)]

        if word1 in self.match_against and word2 in self.match_against:
            return (word1, word2)  
        else:
            return None
    
    def __init__(self, *names):
        from nltk.corpus import words
        self.match_against = words.words()
        self.candidates = []
        for i, name1 in enumerate(names):
            for j, name2 in enumerate(names):
                if i < j:
                    if self.process_names(name1, name2):
                        word1, word2 = self.process_names(name1, name2)
                        self.candidates.append((name1, name2, word1, word2))
        
if __name__ == "__main__":
    print("\n"+problem)
#     print("Run test_politicians to run tests.")
#     # hand-made list
#     # from http://thehill.com/homenews/campaign/215523-the-65-people-who-may-run-for-president-in-2016
# 
#     names = ("Joe",
#              "Joseph",
#              "Jerry",
#              "Hillary",
#              "Andrew",
#              "Russ",
#              "Al",
#              "Maggie",
#              "Margaret",
#              "John",
#              "Amy",
#              "Martin",
#              "Janet",
#              "Jay",
#              "Deval",
#              "Bernie",
#              "Brian",
#              "Mark",
#              "Elizabeth",
#              "Jim",
#              "Kelly",
#              "Michele",
#              "Haley",
#              "Marsha",
#              "John",
#              "Scott",
#              "Jeb",
#              "Herman",
#              "Ben",
#              "Chris",
#              "Ted",
#              "Mitch",
#              "Mary",
#              "Bill",
#              "William",
#              "Newt",
#              "Nikki",
#              "Mike",
#              "Bobby",
#              "Robert",
#              "Pete",
#              "Peter",
#              "Steve",
#              "Steven",
#              "Susana",
#              "Cathy",
#              "Sarah",
#              "Rand",
#              "Mike",
#              "Rick",
#              "Condoleezza",
#              "Mike",
#              "Michael",
#              "Mitt",
#              "Marco",
#              "Paul",
#              "Brian",
#              "Rick",
#              "Joe",
#              "Joseph",
#              "Tim",
#              "Donald",
#              "Don",
#              "Scott",
#              "Allen")
#     s = solution(*names)
#     if len(s.candidates):
#         for candidate in s.candidates:
#             print("Answer could be:{0},{1}-->{2},{3}".format(candidate[0], candidate[1], candidate[2], candidate[3]))
#     else:
#         print("There were no possible answers generated by the hand-crafted list.")
#     print("Done.")
#     print()
    print("from file pols.txt...")
    f = open("pols.txt", "r")
    names = tuple(set([name.split()[0] for name in f.readlines()]))
    f.close()
    s = solution(*names)
    if len(s.candidates):
        for candidate in s.candidates:
            print("Answer could be:{0},{1}-->{2},{3}".format(candidate[0], candidate[1], candidate[2], candidate[3]))
    else:
        print("There were no possible answers generated by the hand-crafted list.")
    print("Done.")
