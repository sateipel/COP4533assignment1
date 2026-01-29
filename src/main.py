from match import gale_shapley
from verify import verify
from scale import make_preferences

def main():
    n = int(input("Enter number of hospitals/students: "))
    hospitals, students = make_preferences(n)

    matches, proposals = gale_shapley(hospitals, students)
    result = verify(matches, hospitals, students)

    print("\nMatching (Hospital -> Student):")
    for h, s in enumerate(matches):
        print(f"H{h} -> S{s}")

    print("\nVerification:", result)
    print("Total proposals:", proposals)

if __name__ == "__main__":
    main()
