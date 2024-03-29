def main():
    students = [
        {"name": "Harry", "house": "Gryffendor", "patronus": "Stag"},
        {"name": "Hermione", "house": "Gryffendor", "patronus": "Otter"},
        {"name": "Ron", "house": "Gryffendor", "patronus": "Jack Russell Terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus": None},
    ]

    for student in students:
        print(student["name"], student["house"], student["patronus"], sep=", ")
    
main()