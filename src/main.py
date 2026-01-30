from match import gale_shapley
from verify import verify
from scale import make_preferences

#read inputs
    #open the file to be able to read from it
    #ensure it opened properly and the correct size (n*2)+1 lines
    #create the empty lists to append the preferences to 
    #based on the first int, go through 2 for loops of length n
    #for loop that will append a list of prefenreces (a line of input) into the list 
    #repeat for loop for students (starts at n+1 lines down)

#write outputs
    #open/create the output file to write to
    #for the hospital/students matches, enumerate the results 
        #write 

#change this in order to be able to read a file OR input from user
def main():
    #FORM: python main.py *inputFile.in* *outputFile.out*
    #if sys.arg=3: file input mode 
        #make variables from file inputs (sys.arg)
        #based on those inputds, call the functions
        #write to output file 
        #print the results
    #else: input from user mode 
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
