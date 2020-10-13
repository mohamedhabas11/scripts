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
            prog = re.compile(r'Basic\s*.etwork\sknowledge+')
            result = prog.match(line)
            return result.group(0)
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
            prog = re.compile(r'[Ee]xperience\swith.+')
            result = prog.finditer(line)
            for match in result:
                print(match.group(0))
                
            pattern = re.compile(r'[Bb]asic\s+[Uu]nderstanding\sof\s.+.*')
            basics = pattern.finditer(line)
            for match in basics:
                print(match.group(0))

            pattern2 = re.compile(r'/*[Aa]bility.+')
            abilities = pattern2.finditer(line)
            for match in abilities:
                print(match.group(0))

            pattern3 = re.compile(r'/*[Ff]luent.+')
            languages = pattern3.finditer(line)
            for match in languages:
                print(match.group(0))

            pattern4 = re.compile(r'/*[Aa]ttention.+')
            softskills = pattern4.finditer(line)
            for match in softskills:
                print(match.group(0))
            
            pattern5 = re.compile(r'[Cc]ustomer.[Oo]riented.[Aa]ttitude+|[Cc]ustomer.[Ss]upport+')
            customer_support = pattern5.finditer(line)
            for match in customer_support:
                print(match.group(0))
            
                
        except AttributeError:
            pass
    return False        


kind_of_engineer = linux()
print(kind_of_engineer)


