#!/usr/bin/python3.4.2
'''
Created on Apr 12, 2015

Think of a job, in 8 letters, that names 
someone who might work with actors. 

Change one letter in this to the 
following letter of the alphabet to 
name another person who works 
with actors. What jobs are these?

@author: john.obrien, leiran.biton
'''

'''
Solve pretty

given a list of jobs, runs solve, and prints the output.
'''


def solve_pretty(jobs):
    solutions = solve(jobs)
    if solutions == []:
        print("No solutions found.")
    else:
        for solution in solutions:
            print("One possible solution is {0} and {1}".format(solution[0], solution[1]))
    return


'''
solve - function to solve this weeks puzzler by
        incrementing each letter to the next
        letter in the alphabet

takes jobs: a list of jobs of people who work with actors

returns solutions: a list of tuples, 
where each tuple is two job titles which
might be the solution

'''

def solve(jobs):
    solutions = []
    # convert all to lower, b/c we check
    # whether new_job is in jobs, so all jobs
    # have to be lower
    
    jobs = [job.lower() for job in jobs]
    for job in jobs:
        # Create a new job title by incrementing each letter by 1
        # within the currrent job title we're looking at
        if len(job) is not 8:
            continue
        for offset, letter in enumerate(job):
            new_letter = chr(ord(letter) + 1)
            new_job = job[:offset] + new_letter + job[offset+1:]
            if new_job in jobs:
                solutions.append((job, str(new_job)))

    return solutions

if __name__ == "__main__":
    print("Dummy data run..")
    jobs = ["director",
            "Eirector"]
    solve_pretty(jobs)
    print("Hand crafted data run...")
    # List of jobs in theater: http://en.wikipedia.org/wiki/List_of_theatre_personnel
    # jobs can only be 8 letters long
    jobs = ["producer",
            "director",
            "designer",
            "waitress",
            ""]
    solve_pretty(jobs)
    print("NlTK Generated data run...")