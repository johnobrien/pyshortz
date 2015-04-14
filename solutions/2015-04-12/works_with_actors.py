#!/usr/local/bin/env python 
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
        for solution in solutions: # reformatted for ease of viewing
            print("    {0} --> {1}".format(solution[0], solution[1]))
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
    from string import ascii_lowercase
    nextletter = "".maketrans(ascii_lowercase,ascii_lowercase[1:]+"a")
    solutions = []
    # convert all to lower, b/c we check
    # whether new_job is in jobs, so all jobs
    # have to be lower
    # note: assumes all jobs are single words
    jobs = [job.lower() for job in jobs]
    for job in jobs:
        # ignore jobs longer than 8 letters
        if len(job) is not 8:
            continue
        # Create a new job title by incrementing each letter by 1
        # within the current job title we're looking at
        
        for offset, letter in enumerate(job):
            new_letter = letter.translate(nextletter)
            new_job = job[:offset] + new_letter + job[offset+1:]
            if new_job in jobs:
                if not (new_job, job) in solutions: # do not add duplicates
                    solutions.append((job, new_job))

    return solutions

if __name__ == "__main__":
    print("Dummy data run...")
    print("Expected matches:")
    print("    director --> eirector")
    print("    traitors --> traitort")
    jobs = ["director",
            "Eirector",
            "waiter",
            "gaiter",
            "gaitor",
            "Traitors",
            "traitorT"
            ]
    print("results:")
    solve_pretty(jobs)
    print("Hand crafted data run...")
    
    # List of jobs in theater: http://en.wikipedia.org/wiki/List_of_theatre_personnel
    # jobs can only be 8 letters long
    jobs = ["producer"
           ,"director"
           ,"designer"
           ,"waitress"
           ,"Playwright"
           ,"Choreographer"
           ,"stagehand"
           ,"writer"
           ,"wrestler"
           ,"supervisor"
           ,"manager"
           ,"publicist"
           ,"usher"
           ,"actor"
           ,"actress"
           ,"waiter"
           ,"critic"
           ,"playwright"
           ,"Dramaturg"
           ,"Dramaturge"
           ,"stagecrew"
           ,"Publicist"
           ,"Showgirl"
           ,"daredevil"
           ,"stuntdouble"
           ] 
    handrun = solve_pretty(jobs)
    print("NlTK Generated data run...")
    print("....not yet implemented!")