# TASK A
#Matching Engine: Implement the hospital-proposing deferred acceptance algorithm
#-Initially, all hospitals are unmatched and have not proposed to anyone.
#-While there exists an unmatched hospital that still has students left to propose to:
#    -The hospital proposes to the next student on its preference list that it has not yet proposed to.
#    -The student tentatively accepts the best hospital (according to the student's preferences) among 
#    its current tentative match (if any) and the new proposer, rejecting the other.

def gale_shapley(hospitalsPref, applicantsPref):
#initialize each person&hospital to be free (and proposal to track)
    num=len (hospitalsPref)
    freeHospitals=list(range(num))
    hospitalMatches=[None]*num
    applicantMatches=[None]*num
    nextProposal = [0] * num
#while (some hospital = free and hasnt been matched/assigned to every applicant):
    while freeHospitals:
        #choose some hospital h
        h=freeHospitals.pop(0)
    #a=1st app on h's list to whom h has not been matched
        #go to next on h's list 
        a=hospitalsPref[h][nextProposal[h]]
        nextProposal[h] += 1
    #if (a is free)
        #assign h to a
        if applicantMatches[a] is None:
            hospitalMatches[h]=a
            applicantMatches[a]=h
    #else if (a prefers h to her current match h')
        #assign h to a & h' has a slot free
        elif applicantsPref[a].index(h) < applicantsPref[a].index(applicantMatches[a]):
            current=applicantMatches[a]
            hospitalMatches[h]=a
            applicantMatches[a]=h
            hospitalMatches[current]=None
            freeHospitals.append(current)
    #else
        #a rejects h
        else: 
            freeHospitals.append(h)
    return hospitalMatches
#could tentatively return number of proposals too by adding counter 