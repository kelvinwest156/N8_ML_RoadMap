import json

# More complex data structure
students = [
    {
        "id": 1,
        "name": "Alice",
        "grades": [85, 90, 92],
        "active": True
    },
    {
        "id": 2,
        "name": "Bob",
        "grades": [78, 88, 95],
        "active": True
    },
    {
        "id": 3,
        "name": "Charlie",
        "grades": [92, 94, 89],
        "active": False
    }
]

# Save to file
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

# Read from file
with open("students.json", "r") as file:
    loaded_students = json.load(file)

# Work with the data
for student in loaded_students:
    avg = sum(student["grades"]) / len(student["grades"])
    print(f"{student['name']}: Average grade = {avg:.2f}")
