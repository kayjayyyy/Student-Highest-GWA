# Templanza, Kristine Joy F.
# BSCPE 1-4
# Asignnment no. 3 - Student with Highest GWA

# Greeting and border line
print("")
print("\033[35m※ \033[0m" * 35)
print("")
print("\033[45m ♥ Welcome to our program! ♥ \033[0m".center(78))

# Ask the name of the user 
name = input("\n\033[033mGood day! What is your name? \033[0m")
print("\n\033[3;33mI hope you are doing well,", name + "!\033[0m")
print("")

# Assign for the GWA value and highest student name
highest_GWA = 5.0
name_of_the_highest_student = ""

# Open StudentsName&GWA.txt (read)
with open("StudentsName&GWA.txt") as input_student_file:
    # Process the loop of the program
    for line in input_student_file:
        record = line.split(",")
        students_name = record[0]
        # Convert GWA to float
        GWA = float(record[1])
        # Check the highest grade
        if GWA < highest_GWA:
            highest_GWA = GWA
            name_of_the_highest_student = students_name

input("\033[3m♥ Press enter to print the student who got the highest GWA\033[0m")

print("")
print("-" * 70)
print("\033[1;3;34mWill print the student with highest GWA....\033[0m".center(80))
print("-" * 70)
print("")

# Print the highest GWA and the student name
print("\033[32;3mName of the student:\033[0m", name_of_the_highest_student)
print("\033[32;3mGWA:\033[0m", highest_GWA)

# Outro and border line
print("\n")
print("\033[3mThank you for supporting our program!".center(70))
print("")
print("\033[35m※ \033[0m" * 35)
print("")