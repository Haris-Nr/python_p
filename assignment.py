
import array as ar
# create calculate average function we use sum methon to plus grades in list and then return average 
def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average
# after function we use try block to enter student name and there grades using while loop 
# we use studentList as "list" and gradesArray as "array"
try:
    studentList = []
    gradesArray = ar.array('i', [])
    
    while True:
        nameStudent = input("Enter Student Name (or press Enter to finish): ")
        
        if not nameStudent:
            break  # Exit the loop if Enter is pressed without entering a name
        studentList.append(nameStudent) # here we append the student name in studentList we get from user 
        
        i = 0
        while i < 6:  # we run this loop 6 times because students subject is 6 and here we also get grades from user after every student name enter: and then we append this in gradesArray
            try:
                gradesStudent = int(input("Enter Student's Grades (or press Enter for the next student): ")) 
                gradesArray.append(gradesStudent)
                i += 1
            except ValueError:
                print("Please enter a valid grade.")
        # after we print student names we use for loop and f-Strings format to show student list
    print("Student List:")
    for i in range(len(studentList)):
        print(f"{studentList[i]}: {gradesArray[i*6:(i+1)*6]}")
    # here we send gradesArray as argument parameter in calculate_average function
    average = calculate_average(gradesArray)
    print("Average Grade:", average)
    
except NameError:
    print("Enter the right command")
