#!/usr/bin/env python3
import re
def check(word):
    with open('job_description.txt') as job_description:
        datafile = job_description.readlines()
    for line in datafile:
        if word in line:
            # found = True # Not necessary
            return True
    return False  # Because you finished the search without finding

#print(check("tasks"))

def what_am_i_doing():
    with open('job_description.txt') as job_description:
        datafile = job_description.readlines()
    for line in datafile:
        prog = re.compile(r'/*.+Engineer')
        result = prog.match(line)
        return result.group()
    return False        


kind_of_engineer = what_am_i_doing()
print(kind_of_engineer)
