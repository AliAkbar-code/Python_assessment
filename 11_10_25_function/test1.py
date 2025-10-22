students = {
    "Ali": {"Math": 85, "Science": 90, "English": 88, "History": 78},
    "Maryam": {"Math": 92, "Science": 89, "English": 94, "History": 80},
    "Minahil": {"Math": 73, "Science": 78, "English": 82, "History": 70},
    "Farooq": {"Math": 87, "Science": 85, "English": 90, "History": 76}
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
            for name, subjects in students.items():
                print(f"{name}:")
                for subject, mark in subjects.items():
                    print(f"  {subject}: {mark}")

    # 2️⃣ View One Student's Marks
    elif choice == "2":
        while True:
            name = input("Enter student name: ").capitalize()
            if not name.isalpha():
                print("⚠️ Invalid name! Please enter letters only.")
                continue
            if name in students:
                print(f"{name}'s Marks:")
                for subject, mark in students[name].items():
                    print(f"  {subject}: {mark}")
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
                    subjects = {}
                    for subject in ["Math", "Science", "English", "History"]:
                        while True:
                            try:
                                mark = int(input(f"Enter marks for {subject}: "))
                                if mark < 0 or mark > 100:
                                    print("⚠️ Marks must be between 0 and 100.")
                                    continue
                                subjects[subject] = mark
                                break
                            except ValueError:
                                print("⚠️ Please enter a valid number for marks.")
                    students[name] = subjects
                    print(f"✅ {name} added successfully!")
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
                    print(f"Current marks for {name}:")
                    for subject, mark in students[name].items():
                        print(f"  {subject}: {mark}")
                    subject = input("Enter subject to update: ").capitalize()
                    if subject in students[name]:
                        while True:
                            try:
                                new_marks = int(input(f"Enter new marks for {subject}: "))
                                if new_marks < 0 or new_marks > 100:
                                    print("⚠️ Marks must be between 0 and 100.")
                                    continue
                                students[name][subject] = new_marks
                                print(f"✅ Marks updated for {subject}!")
                                break
                            except ValueError:
                                print("⚠️ Please enter a valid number for marks.")
                    else:
                        print("❌ Subject not found!")
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
            for name, subjects in students.items():
                total_marks = sum(subjects.values())
                average = total_marks / len(subjects)
                if average >= 90:
                    grade = "A+"
                elif average >= 80:
                    grade = "A"
                elif average >= 70:
                    grade = "B"
                elif average >= 60:
                    grade = "C"
                else:
                    grade = "Fail"
                print(f"{name}: Average Marks = {average:.2f}, Grade = {grade}")

    # 6️⃣ View One Student's Grade
    elif choice == "6":
        while True:
            try:
                name = input("Enter student name to view grade: ").capitalize()
                if not name.isalpha():
                    raise ValueError("Name must contain only letters.")
                if name in students:
                    total_marks = sum(students[name].values())
                    average = total_marks / len(students[name])
                    if average >= 90:
                        grade = "A+"
                    elif average >= 80:
                        grade = "A"
                    elif average >= 70:
                        grade = "B"
                    elif average >= 60:
                        grade = "C"
                    else:
                        grade = "Fail"
                    print(f"{name}: Average Marks = {average:.2f}, Grade = {grade}")
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
