# TASK B
#Verifier
#Write a separate program (or a separate mode in the same program) that:
#(a)  Checks validity: each hospital and each student is matched to exactly 
# one partner, with no duplicates. And (b) checks stability: confirms there 
# is no blocking pair.

#define the function and take in the output of match as this one's input 
def verify(hospitalMatches, hospitalsPref, applicantsPref):
    num=len (hospitalMatches)
    #part a: validity 
    #check that there is no loners 
    if None in hospitalMatches:
        return "Invalid (something is unmatched)"
    #create an empty set for applicants and hospitals to track matches
    matchedApplicants=set()
    matchedHospitals=set()
    #for each h in hospital, check which applicant its matched too
        #if that applicant is already in the set (already macthed elsewhere)
            # return false (not valid)
        #otherwise, add to set (valid)
        # move onto the next hospital 
    for h in range(num):
        applicant=hospitalMatches[h]
        if applicant in matchedApplicants:
            return "Invalid (applicant matched multiple times)"
        matchedApplicants.add(applicant)
    #for each a in applicants, check which hospital its matched too
        #if that hospital is already in the set (already macthed elsewhere) 
            # return false (not valid)
        #otherwise, add to set (valid)
        # move onto the next applicant 
    for a in range(num):
        hospital=hospitalMatches.index(a)
        if hospital in matchedHospitals:
            return "Invalid (hospital matched multiple times)"
        matchedHospitals.add(hospital)
    #part b: stability (nested for loop?) 
        #for h in hospitals
            #for a in applicants
                #if h prefers a to its current
                    #if a prefers h to its current match
                        #return false (not stable)
    #**i think this part could potentially be optimized??**
    for h in range(num):
        currApp = hospitalMatches[h]
        for a in range(num):
            currHosp=hospitalMatches.index(a)
            if (hospitalsPref[h].index(a) < hospitalsPref[h].index(currApp)):
                if (applicantsPref[a].index(h) < applicantsPref[a].index(currHosp)):
                    return "Invalid (unstable match found)"
    #return true (stable & valid)
    return "Verified (stable and valid)"