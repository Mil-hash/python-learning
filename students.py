students = []

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print(name + " added!")

def remove_student():
    name = input("Enter student name to remove: ")
    if name in students:
        students.remove(name)
        print(name + " removed!")
    else:
        print("student not found!")

def search_student():
    name = input("Enter student name to search: ")
    if name in students:
        print(name + " is in the list!")
    else:
        print("student not found!")

def display_all():
    print("students:")
    for student in students:
        print("- " + student)
while True:
    print("\n1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        display_all()
    elif choice == "5":
        print("")
        break
    else:
        print("Invalid choice!")