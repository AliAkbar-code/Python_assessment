# # 🎓 Multi-Student Grade Manager

# students = []  # list to hold all student records

# # Function to calculate and display report
# def show_report(student):
#     name, subjects, marks = student
#     total = sum(marks)
#     average = total / len(marks)
#     highest = max(marks)
#     lowest = min(marks)
#     unique_marks = set(marks)

#     # Grade system
#     if average >= 90:
#         grade = "A"
#     elif average >= 75:
#         grade = "B"
#     elif average >= 60:
#         grade = "C"
#     elif average >= 40:
#         grade = "D"
#     else:
#         grade = "F"

#     highest_subject = subjects[marks.index(highest)]
#     lowest_subject = subjects[marks.index(lowest)]

#     print(f"\n📊 Report for {name}")
#     print("-" * 35)
#     for i in range(len(subjects)):
#         print(f"{subjects[i]}: {marks[i]}")
#     print("\nTotal Marks:", total)
#     print("Average Marks:", round(average, 2))
#     print("Highest Marks:", highest, f"({highest_subject})")
#     print("Lowest Marks:", lowest, f"({lowest_subject})")
#     print("Unique Marks:", unique_marks)
#     print("Final Grade:", grade)


# # Function to find topper
# def find_topper():
#     if not students:
#         print("No student records found!")
#         return

#     topper = None
#     top_avg = 0

#     for student in students:
#         name, subjects, marks = student
#         avg = sum(marks) / len(marks)
#         if avg > top_avg:
#             top_avg = avg
#             topper = name

#     print(f"\n🏆 Topper: {topper} with average {round(top_avg, 2)}")


# # Main menu
# while True:
#     print("\n==== Multi-Student Grade Manager ====")
#     print("1. Add New Student")
#     print("2. Show Report of One Student")
#     print("3. Show Report of All Students")
#     print("4. Find Topper")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         name = input("Enter student name: ")
#         num_subjects = int(input(f"How many subjects for {name}? "))
#         subjects = []
#         marks = []

#         for i in range(num_subjects):
#             subject = input(f"Enter subject {i+1} name: ")
#             mark = int(input(f"Enter marks for {subject}: "))
#             subjects.append(subject)
#             marks.append(mark)

#         students.append((name, tuple(subjects), marks))
#         print(f"Student {name} added successfully!")

#     elif choice == "2":
#         search_name = input("Enter student name to view report: ")
#         found = False
#         for student in students:
#             if student[0].lower() == search_name.lower():
#                 show_report(student)
#                 found = True
#                 break
#         if not found:
#             print("Student not found!")

#     elif choice == "3":
#         if not students:
#             print("No student records available.")
#         else:
#             for student in students:
#                 show_report(student)

#     elif choice == "4":
#         find_topper()

#     elif choice == "5":
#         print("Exiting program. Goodbye 👋")
#         break

#     else:
#         print("Invalid choice. Try again.")
# #   s2 e5 e8
# # s3 e5 to 8








# 🎓 Multi-Student Grade Manager (No Functions + Error Handling)

students = []  # list to hold all student records

# Main menu
while True:
    print("\n==== Multi-Student Grade Manager ====")
    print("1. Add New Student")
    print("2. Show Report of One Student")
    print("3. Show Report of All Students")
    print("4. Find Topper")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ").capitalize()

        # Safe input for number of subjects
        while True:
            try:
                num_subjects = int(input(f"How many subjects for {name} ? "))
                break
            except ValueError:
                print("❌ Please enter a valid number for subjects.")

        subjects = []
        marks = []

        for i in range(num_subjects):
            subject = input(f"Enter subject {i+1} name: ").capitalize()

            # Safe input for marks
            while True:
                try:
                    mark = int(input(f"Enter marks for {subject}: "))
                    break
                except ValueError:
                    print("❌ Please enter a valid number for marks.")

            subjects.append(subject)
            marks.append(mark)

        students.append((name, tuple(subjects), marks))
        print(f"✅ Student {name} added successfully!")

    elif choice == "2":
        search_name = input("Enter student name to view report: ")
        found = False
        for student in students:
            if student[0].lower() == search_name.lower().capitalize():
                name, subjects, marks = student
                total = sum(marks)
                average = total / len(marks)
                highest = max(marks)
                lowest = min(marks)
                unique_marks = set(marks)

                # Grade system
                if average >= 90:
                    grade = "A"
                elif average >= 75:
                    grade = "B"
                elif average >= 60:
                    grade = "C"
                elif average >= 40:
                    grade = "D"
                else:
                    grade = "F"

                highest_subject = subjects[marks.index(highest)]
                lowest_subject = subjects[marks.index(lowest)]

                print(f"\n📊 Report for {name}")
                print("-" * 35)
                for i in range(len(subjects)):
                    print(f"{subjects[i]}: {marks[i]}")
                print("\nTotal Marks:", total)
                print("Average Marks:", round(average, 2))
                print("Highest Marks:", highest, f"({highest_subject})")
                print("Lowest Marks:", lowest, f"({lowest_subject})")
                print("Unique Marks:", unique_marks)
                print("Final Grade:", grade)

                found = True
                break
        if not found:
            print("⚠️ Student not found!")

    elif choice == "3":
        if not students:
            print("⚠️ No student records available.")
        else:
            for student in students:
                name, subjects, marks = student
                total = sum(marks)
                average = total / len(marks)
                highest = max(marks)
                lowest = min(marks)
                unique_marks = set(marks)

                if average >= 90:
                    grade = "A"
                elif average >= 75:
                    grade = "B"
                elif average >= 60:
                    grade = "C"
                elif average >= 40:
                    grade = "D"
                else:
                    grade = "F"

                highest_subject = subjects[marks.index(highest)]
                lowest_subject = subjects[marks.index(lowest)]

                print(f"\n📊 Report for {name}")
                print("-" * 35)
                for i in range(len(subjects)):
                    print(f"{subjects[i]}: {marks[i]}")
                print("\nTotal Marks:", total)
                print("Average Marks:", round(average, 2))
                print("Highest Marks:", highest, f"({highest_subject})")
                print("Lowest Marks:", lowest, f"({lowest_subject})")
                print("Unique Marks:", unique_marks)
                print("Final Grade:", grade)

    elif choice == "4":
        if not students:
            print("⚠️ No student records found!")
        else:
            topper = None
            top_avg = 0
            for student in students:
                name, subjects, marks = student
                avg = sum(marks) / len(marks)
                if avg > top_avg:
                    top_avg = avg
                    topper = name
            print(f"\n🏆 Topper: {topper} with average {round(top_avg, 2)}")

    elif choice == "5":
        print("Exiting program. Goodbye 👋")
        break

    else:
        print("❌ Invalid choice. Try again.")
