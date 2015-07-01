'''
Created on Jun 30, 2015

@author: Leiran Biton, John O'Brien
'''
from solver.solver import Solver
from solver.lists import get_companies, get_musicians


class CompanySingerSolver(Solver):
    '''
    The solver for the 6/28/2015 puzzle.
    '''

    def solve(self):
        companies = get_companies()
        musicians = get_musicians()
        
        for company in companies:
            parts = company.split()
            if len(parts)== 2:
                candidate = parts[0][1:] + " " + parts[1][:-1]
                if candidate in musicians:
                    print(candidate.encode("utf-8"))

if __name__ == '__main__':

    p = """
Name a major American company. Drop its first and last letters, 
and the remaining letters in order will name a famous singer -
both first and last names. What company is it?
"""

    s = CompanySingerSolver(puzzle_text = p, verbose=False)
    s.solve()
