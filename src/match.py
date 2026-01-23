# TASK A
#Matching Engine: Implement the hospital-proposing deferred acceptance algorithm
#-Initially, all hospitals are unmatched and have not proposed to anyone.
#-While there exists an unmatched hospital that still has students left to propose to:
#    -The hospital proposes to the next student on its preference list that it has not yet proposed to.
#    -The student tentatively accepts the best hospital (according to the student's preferences) among 
#    its current tentative match (if any) and the new proposer, rejecting the other.