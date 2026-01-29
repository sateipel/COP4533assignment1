# TASK C
# Scalability
#Measure the running time of your matching engine on an increasingly larger number of 
# hospitals/students, i.e., n = 1, 2, 4, 8, 16, 32, 64, 128, 256, 512 and graph the 
# running time as a line graph when n on the x-axis and the running time on the y-axis.
#   Do the same for the verified.  What is the trend that you notice? Note: How you measure 
# the running time is up to you (there are multiple ways of doing this) and will likely 
# depend on which programming language you choose.

import time
import random
import matplotlib.pyplot as plt

def generate_random_preferences(n):
    """Generate random preference lists for n hospitals and n students"""
    hospitals = []
    students = []
    
    for i in range(n):
        pref = list(range(n))
        random.shuffle(pref)
        hospitals.append(pref)
    
    for i in range(n):
        pref = list(range(n))
        random.shuffle(pref)
        students.append(pref)
    
    return hospitals, students


def gale_shapley(hospitalsPref, applicantsPref):
    """Gale-Shapley algorithm"""
    num = len(hospitalsPref)
    freeHospitals = list(range(num))
    hospitalMatches = [None] * num
    applicantMatches = [None] * num
    nextProposal = [0] * num
    
    while freeHospitals:
        h = freeHospitals.pop(0)
        a = hospitalsPref[h][nextProposal[h]]
        nextProposal[h] += 1
        
        if applicantMatches[a] is None:
            hospitalMatches[h] = a
            applicantMatches[a] = h
        elif applicantsPref[a].index(h) < applicantsPref[a].index(applicantMatches[a]):
            current = applicantMatches[a]
            hospitalMatches[h] = a
            applicantMatches[a] = h
            hospitalMatches[current] = None
            freeHospitals.append(current)
        else:
            freeHospitals.append(h)
    
    return hospitalMatches
