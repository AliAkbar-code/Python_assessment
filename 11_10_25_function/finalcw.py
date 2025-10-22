students = {
    "Ali": 100,
    "Maryam": 100,
    "Minahil": 100,
    "Farooq": 100
}

while True:
    print("\n===== 🎓 Student Grade Calculator =====")
    print("1. View All Students' Marks")
    print("2. View One Student's Marks")
    print("3. Add New Student")
    print("4. Update Marks")
    print("5. Calculate Grades (All Students)")
    print("6. View One Student's Grade")
    print("7. Remove Student")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    # 1️⃣ View All Students
    if choice == "1":
        print("\n📘 All Students' Marks:")
        if len(students) == 0:
            print("No students found!")
        else:
            for name, mark in students.items():
                print(f"{name}: {mark}")

    # 2️⃣ View One Student's Marks
    elif choice == "2":
        while True:
            name = input("Enter student name: ").capitalize()
            if not name.isalpha():
                print("⚠️ Invalid name! Please enter letters only.")
                continue
            if name in students:
                print(f"{name}'s Marks: {students[name]}")
                break
            else:
                print("❌ Student not found!")
                break

    # 3️⃣ Add New Student
    elif choice == "3":
        while True:
            try:
                name = input("Enter new student name: ").capitalize()
                if not name.isalpha():
                    raise ValueError("Name must contain only letters.")
                if name in students:
                    print("⚠️ Student already exists!")
                    break
                else:
                    while True:
                        try:
                            marks = int(input(f"Enter marks for {name}: "))
                            if marks < 0 or marks > 100:
                                print("⚠️ Marks must be between 0 and 100.")
                                continue
                            students[name] = marks
                            print(f"✅ {name} added successfully!")
                            break
                        except ValueError:
                            print("⚠️ Please enter a valid number for marks.")
                    break
            except ValueError as e:
                print(f"⚠️ Invalid input: {e}")

    # 4️⃣ Update Marks
    elif choice == "4":
        while True:
            try:
                name = input("Enter student name to update marks: ").capitalize()
                if not name.isalpha():
                    raise ValueError("Name must contain only letters.")
                if name in students:
                    while True:
                        try:
                            new_marks = int(input(f"Enter new marks for {name}: "))
                            if new_marks < 0 or new_marks > 100:
                                print("⚠️ Marks must be between 0 and 100.")
                                continue
                            students[name] = new_marks
                            print(f"✅ Marks updated for {name}!")
                            break
                        except ValueError:
                            print("⚠️ Please enter a valid number for marks.")
                    break
                else:
                    print("❌ Student not found!")
                    break
            except ValueError as e:
                print(f"⚠️ Invalid input: {e}")

    # 5️⃣ Calculate Grades (All Students)
    elif choice == "5":
        print("\n📊 Student Grades:")
        if len(students) == 0:
            print("No students available to calculate grades.")
        else:
            for name, mark in students.items():
                if mark >= 90:
                    grade = "A+"
                elif mark >= 80:
                    grade = "A"
                elif mark >= 70:
                    grade = "B"
                elif mark >= 60:
                    grade = "C"
                else:
                    grade = "Fail"
                print(f"{name}: Marks = {mark}, Grade = {grade}")

    # 6️⃣ View One Student's Grade
    elif choice == "6":
        while True:
            try:
                name = input("Enter student name to view grade: ").capitalize()
                if not name.isalpha():
                    raise ValueError("Name must contain only letters.")
                if name in students:
                    mark = students[name]
                    if mark >= 90:
                        grade = "A+"
                    elif mark >= 80:
                        grade = "A"
                    elif mark >= 70:
                        grade = "B"
                    elif mark >= 60:
                        grade = "C"
                    else:
                        grade = "Fail"
                    print(f"{name}: Marks = {mark}, Grade = {grade}")
                    break
                else:
                    print("❌ Student not found!")
                    break
            except ValueError as e:
                print(f"⚠️ Invalid input: {e}")

    # 7️⃣ Remove Student
    elif choice == "7":
        while True:
            try:
                name = input("Enter student name to remove: ").capitalize()
                if not name.isalpha():
                    raise ValueError("Name must contain only letters.")
                if name in students:
                    confirm = input(f"Are you sure you want to remove {name}? (yes/no): ").lower()
                    if confirm == "yes":
                        del students[name]
                        print(f"✅ {name} has been removed successfully.")
                    else:
                        print("❌ Operation cancelled.")
                    break
                else:
                    print("❌ Student not found!")
                    break
            except ValueError as e:
                print(f"⚠️ Invalid input: {e}")

    # 8️⃣ Exit
    elif choice == "8":
        print("👋 Exiting program. Goodbye!")
        break

    else:
        print("❌ Invalid choice! Please enter between 1-8.")
