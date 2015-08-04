from solver.solver import Solver
from solver.lists import get_animals


def first_vowel(word):
    vowels = "aeiou"
    word = word.lower()
    for i in range(0, len(word)):
        if word[i] in vowels:
            return i


class SpooningAnimalsSolver(Solver):
    def solve(self, animals):
        candidates = []
        for a1 in animals:
            for a2 in animals:
                if self.__dict__.get("verbose", False):
                    print("Trying {0} and {1}".format(a1, a2))
                offset_1 = first_vowel(a1)
                offset_2 = first_vowel(a2)
                word1 = a1[0:offset_1] + a2[offset_2:]
                word2 = a2[0:offset_2] + a1[offset_1:]
                new_a1 = " ".join([word1, word2])
                if new_a1 in animals:
                    candidates.append((a1, a2, new_a1))

        return candidates

if __name__ == '__main__':

    p = """
Name two animals. Exchange their initial consonant sounds,
and the result in two words will be the name of a third animal.
What is it?
"""

    s = SpooningAnimalsSolver(puzzle_text=p,
                              verbose=True)
    print(s.solve(animals=get_animals()))
