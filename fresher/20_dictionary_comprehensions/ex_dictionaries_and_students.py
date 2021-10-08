# This coding exercise has three parts. See them outlined in detail in the coding exercise,
# as comments.

# Create a dictionary variable, called student .
# Modify a variable, grades , so it contains the value of a dictionary's key.
# Implement a function calculating a total average grade for a class of students.

# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', 'grades'
# The values for each must be 'Jose', 'Computing' and a tuple with the values 66, 77, and 88

student = {"name": "Jose", "school": "Computing", "grades": (66, 77, 88)}


def average_grade(data):
    grades = data["grades"]
    return sum(grades) / len(grades)


print(average_grade(student))


def average_grage_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student["grades"])
        count += len(student["grades"])

    return total / count
