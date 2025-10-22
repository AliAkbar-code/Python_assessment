# # 🎓 Student Grade Calculator (Three Students, One Subject Each, Can Add More)

# # Hardcoded initial data
# students = {
#     "Ali": 85,
#     "Sara": 92,
#     "Ahmed": 73
# }

# while True:
#     print("\n===== 🎓 Student Grade Calculator =====")
#     print("1. View All Students' Marks")
#     print("2. View One Student's Marks")
#     print("3. Add New Student")
#     print("4. Update Marks")
#     print("5. Calculate Grades")
#     print("6. Exit")

#     choice = input("Enter your choice (1-6): ")

#     # 1️⃣ View All Students
#     if choice == "1":
#         print("\n📘 All Students' Marks:")
#         if len(students) == 0:
#             print("No students found!")
#         else:
#             for name, mark in students.items():
#                 print(f"{name}: {mark}")

#     # 2️⃣ View One Student
#     elif choice == "2":
#         name = input("Enter student name: ").capitalize()
#         if name in students:
#             print(f"{name}'s Marks: {students[name]}")
#         else:
#             print("❌ Student not found!")

#     # 3️⃣ Add New Student
#     elif choice == "3":
#         name = input("Enter new student name: ").capitalize()
#         if name in students:
#             print("⚠️ Student already exists!")
#         else:
#             marks = int(input(f"Enter marks for {name}: "))
#             students[name] = marks
#             print(f"✅ {name} added successfully!")

#     # 4️⃣ Update Marks
#     elif choice == "4":
#         name = input("Enter student name to update marks: ").capitalize()
#         if name in students:
#             new_marks = int(input(f"Enter new marks for {name}: "))
#             students[name] = new_marks
#             print(f"✅ Marks updated for {name}!")
#         else:
#             print("❌ Student not found!")

#     # 5️⃣ Calculate Grades
#     elif choice == "5":
#         print("\n📊 Student Grades:")
#         if len(students) == 0:
#             print("No students available to calculate grades.")
#         else:
#             for name, mark in students.items():
#                 if mark >= 90:
#                     grade = "A+"
#                 elif mark >= 80:
#                     grade = "A"
#                 elif mark >= 70:
#                     grade = "B"
#                 elif mark >= 60:
#                     grade = "C"
#                 else:
#                     grade = "Fail"
#                 print(f"{name}: Marks = {mark}, Grade = {grade}")

#     # 6️⃣ Exit
#     elif choice == "6":
#         print("👋 Exiting program. Goodbye!")
#         break

#     else:
#         print("❌ Invalid choice! Please enter between 1-6.")



# 🎓 Student Grade Calculator (Three Students, One Subject Each, Can Add More)

# Hardcoded initial data
# students = {
#     "Ali": 85,
#     "Maryam": 92,
#     "Minahil": 73,
#     "Farooq":87
# }

# while True:
#     print("\n===== 🎓 Student Grade Calculator =====")
#     print("1. View All Students' Marks")
#     print("2. View One Student's Marks")
#     print("3. Add New Student")
#     print("4. Update Marks")
#     print("5. Calculate Grades (All Students)")
#     print("6. View One Student's Grade")
#     print("7. Exit")

#     choice = input("Enter your choice (1-7): ")

#     # 1️⃣ View All Students
#     if choice == "1":
#         print("\n📘 All Students' Marks:")
#         if len(students) == 0:
#             print("No students found!")
#         else:
#             for name, mark in students.items():
#                 print(f"{name}: {mark}")

#     # 2️⃣ View One Student's Marks
#     elif choice == "2":
#         name = input("Enter student name: ").capitalize()
#         if name in students:
#             print(f"{name}'s Marks: {students[name]}")
#         else:
#             print("❌ Student not found!")

#     # 3️⃣ Add New Student
#     elif choice == "3":
#         name = input("Enter new student name: ").capitalize()
#         if name in students:
#             print("⚠️ Student already exists!")
#         else:
#             marks = int(input(f"Enter marks for {name}: "))
#             students[name] = marks
#             print(f"✅ {name} added successfully!")

#     # 4️⃣ Update Marks
#     elif choice == "4":
#         name = input("Enter student name to update marks: ").capitalize()
#         if name in students:
#             new_marks = int(input(f"Enter new marks for {name}: "))
#             students[name] = new_marks
#             print(f"✅ Marks updated for {name}!")
#         else:
#             print("❌ Student not found!")

#     # 5️⃣ Calculate Grades (All Students)
#     elif choice == "5":
#         print("\n📊 Student Grades:")
#         if len(students) == 0:
#             print("No students available to calculate grades.")
#         else:
#             for name, mark in students.items():
#                 if mark >= 90:
#                     grade = "A+"
#                 elif mark >= 80:
#                     grade = "A"
#                 elif mark >= 70:
#                     grade = "B"
#                 elif mark >= 60:
#                     grade = "C"
#                 else:
#                     grade = "Fail"
#                 print(f"{name}: Marks = {mark}, Grade = {grade}")

#     # 6️⃣ View One Student's Grade
#     elif choice == "6":
#         name = input("Enter student name to view grade: ").capitalize()
#         if name in students:
#             mark = students[name]
#             if mark >= 90:
#                 grade = "A+"
#             elif mark >= 80:
#                 grade = "A"
#             elif mark >= 70:
#                 grade = "B"
#             elif mark >= 60:
#                 grade = "C"
#             else:
#                 grade = "Fail"
#             print(f"{name}: Marks = {mark}, Grade = {grade}")
#         else:
#             print("❌ Student not found!")

#     # 7️⃣ Exit
#     elif choice == "7":
#         print("👋 Exiting program. Goodbye!")
#         break

#     else:
#         print("❌ Invalid choice! Please enter between 1-7.")



students = {
    "Ali": 85,
    "Maryam": 92,
    "Minahil": 73,
    "Farooq": 87
}

while True:
    print("\n=====  Student Grade Calculator =====")
    print("1. View All Students' Marks")
    print("2. View One Student's Marks")
    print("3. Add New Student")
    print("4. Update Marks")
    print("5. Calculate Grades (All Students)")
    print("6. View One Student's Grade")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

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
            name = input("Enter new student name: ").capitalize()
            if not name.isalpha():
                print("⚠️ Invalid name! Please enter letters only.")
                continue
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

    # 4️⃣ Update Marks
    elif choice == "4":
        while True:
            name = input("Enter student name to update marks: ").capitalize()
            if not name.isalpha():
                print("⚠️ Invalid name! Please enter letters only.")
                continue
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
            name = input("Enter student name to view grade: ").capitalize()
            if not name.isalpha():
                print("⚠️ Invalid name! Please enter letters only.")
                continue
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

    # 7️⃣ Exit
    elif choice == "7":
        print("👋 Exiting program. Goodbye!")
        break

    else:
        print("❌ Invalid choice! Please enter between 1-7.")
