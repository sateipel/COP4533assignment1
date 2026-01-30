import sys
from match import gale_shapley
from verify import verify
from scale import make_preferences
import os

#read inputs
def fileIn(input):
    #open the file to be able to read from it
    lines=[]
    with open(input, "r") as file:
        for line in file:
            line=line.strip()
            lines.append(line)
    #based on the first int, go through 2 for loops of length n
    n=int(lines[0])
    #ensure it opened properly and the correct size (n*2)+1 lines
    if len(lines)!=(n*2)+1:
        print("Error: incorrect file input")
        return
    #create the empty lists to append the preferences to 
    hospitalPrefs=[]
    studentPrefs=[]
    #for loop that will append a list of prefenreces (a line of input) into the list 
    for i in range(1, n+1):
        prefs=[int(x)-1 for x in lines[i].split()]
        hospitalPrefs.append(prefs)
    #repeat for loop for students (starts at n+1 lines down)
    for j in range(n+1, (n*2)+1):
        prefs=[int(x)-1 for x in lines[j].split()]
        studentPrefs.append(prefs)
    return hospitalPrefs, studentPrefs, n


#write outputs
def fileOut(input, hospitalMatches):
    #open/create the output file to write to
    filename, extention=os.path.splitext(input)
    output=filename+ ".out"
    #for the hospital/students matches, enumerate the results 
    #write 
    with open (output, "w") as file:
        for h,s in enumerate(hospitalMatches):
            file.write(f"{h+1} {s+1}\n")

def main():
    #FORM: python3 main.py *inputFile.in* 
    #if sys arg=2: file input mode 
    if len(sys.argv) == 2:
        #make variables from file inputs (sys.arg)
        input_file = sys.argv[1]
        hospitalsPref, applicantsPref, n = fileIn(input_file)
        #based on those inputds, call the functions
        matches, proposals = gale_shapley(hospitalsPref, applicantsPref)
        result = verify(matches, hospitalsPref, applicantsPref)
        #write to output file 
        #print the results
        for h,s in enumerate(matches):
            print(f"{h+1} {s+1}")
        fileOut(input_file, matches)
        print("\nVerification:", result)
        print("Total proposals:", proposals)
    #else: input from user mode
    else: 
        n = int(input("Enter number of hospitals/students: "))
        hospitals, students = make_preferences(n)

        matches, proposals = gale_shapley(hospitals, students)
        result = verify(matches, hospitals, students)

        print("\nMatching (Hospital -> Student):")
        for h, s in enumerate(matches):
            print(f"{h+1} {s+1}")

        print("\nVerification:", result)
        print("Total proposals:", proposals)
if __name__ == "__main__":
    main()