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

# Print the highest GWA and the student name
print(name_of_the_highest_student, highest_GWA)