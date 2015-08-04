from solver.solver import Solver
from solver.lists import get_animals


class SpooningAnimalsSolver(Solver):
    def solve(self, animals):
        return None
        # Returns possible solutions as list of tuples

if __name__ == '__main__':

    p = """
Name two animals. Exchange their initial consonant sounds,
and the result in two words will be the name of a third animal.
What is it?
"""

    s = SpooningAnimalsSolver(puzzle_text=p,
                              verbose=True)
    print(s.solve(animals=get_animals()))
