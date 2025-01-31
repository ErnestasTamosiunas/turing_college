import csv


# with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(",")
#        print(f"{name} is in {house}")

students = []


with open("students.csv") as file:
    # for line in file:
    #    name, house = line.rstrip().split(",")
    #    # student = {}
    #    # student["name"] = name
    #    # student["house"] = house
    #    student = {"name": name, "house": house}
    #    students.append(student)
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
