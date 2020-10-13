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

def cloud():
    with open('job_description.txt') as job_description:
        datafile = job_description.readlines()
    for line in datafile:
        try:
            prog = re.compile(r'/*.+([Kk]ubernetes)+.*')
            result = prog.match(line)
            return result.group()
        except AttributeError:
            pass
    return False        


kind_of_engineer = cloud()
print(kind_of_engineer)



def linux():
    with open('job_description.txt') as job_description:
        datafile = job_description.readlines()
    for line in datafile:
        try:
            prog = re.compile(r'/*.+( [A-z]nix)')
            result = prog.match(line)
            return result.group(1)
        except AttributeError:
            pass
    return False        


kind_of_engineer = linux()
print(kind_of_engineer)


