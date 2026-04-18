students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        students.append({"name": name, "roll": roll})
        print("Student added successfully!")

    elif choice == '2':
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List:")
            for s in students:
                print("Name:", s["name"], "| Roll:", s["roll"])

    elif choice == '3':
        roll = input("Enter roll number to delete: ")
        found = False
        for s in students:
            if s["roll"] == roll:
                students.remove(s)
                print("Student deleted.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")