import time
import random
import matplotlib.pyplot as plt

# generate random rankings
def random_order(n):
    # creates a list and randomly shuffles the list, returning the randomized order
    nums = list(range(n))
    random.shuffle(nums)
    return nums

# generates the random preference list for each hospital
# map() calls random_order(size) 'size' times
def make_preferences(size):
    hospital_rankings = list(map(lambda _: random_order(size), range(size)))
    student_rankings = list(map(lambda _: random_order(size), range(size)))
    return hospital_rankings, student_rankings


def stable_match(hosp_rank, stud_rank):
    total = len(hosp_rank)
    open_hospitals = list(range(total))

    # match tracking: student matched to hospital h
    # hospital matched to student s
    # tracks which student each hospital will propose to next
    hosp_to_student = [None] * total
    student_to_hosp = [None] * total
    proposal_index = [0] * total

    # continues until every hospital is matched
    while open_hospitals:
        hosp = open_hospitals.pop(0)
        stud = hosp_rank[hosp][proposal_index[hosp]]
        proposal_index[hosp] += 1

        if student_to_hosp[stud] is None:
            hosp_to_student[hosp] = stud
            student_to_hosp[stud] = hosp

        # if the student prefers this hospital over their current one -> switch
        elif stud_rank[stud].index(hosp) < stud_rank[stud].index(student_to_hosp[stud]):
            old = student_to_hosp[stud]
            hosp_to_student[hosp] = stud
            student_to_hosp[stud] = hosp
            hosp_to_student[old] = None
            open_hospitals.append(old)

        else:
            open_hospitals.append(hosp)

    # return final hospital -> student matching
    return hosp_to_student


def check_matching(assignments, hosp_rank, stud_rank):
    size = len(assignments)

    if None in assignments:
        return "Invalid"

    seen = set()
    for hosp in range(size):
        stud = assignments[hosp]
        if stud in seen:
            return "Invalid"
        seen.add(stud)

    for hosp in range(size):
        current_student = assignments[hosp]
        for stud in range(size):
            current_hosp = assignments.index(stud)

            if hosp_rank[hosp].index(stud) < hosp_rank[hosp].index(current_student):
                if stud_rank[stud].index(hosp) < stud_rank[stud].index(current_hosp):
                    return "Unstable"

    return "Valid stable"


sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

matching_times = []
verifier_times = []

