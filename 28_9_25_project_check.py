# tasks = []

# def show_menu():
#     print("\n--- To-Do List Menu ---")
#     print("1. View Tasks")
#     print("2. Add Task")
#     print("3. Remove Task")
#     print("4. Mark Task as Done")
#     print("5. Exit")

# while True:
#     show_menu()
#     choice = input("Enter your choice (1-5): ")

#     # View tasks
#     if choice == "1":
#         if not tasks:
#             print("✅ No tasks found!")
#         else:
#             print("\nYour Tasks:")
#             for i, task in enumerate(tasks, 1):
#                 status = "✔ Done" if task["done"] else "❌ Not Done"
#                 print(f"{i}. {task['title']} - {status}")

#     # Add a new task
#     elif choice == "2":
#         title = input("Enter task name: ")
#         tasks.append({"title": title, "done": False})
#         print(f"✅ Task '{title}' added!")

#     # Remove a task
#     elif choice == "3":
#         if not tasks:
#             print("⚠ No tasks to remove!")
#         else:
#             task_num = int(input("Enter task number to remove: "))
#             if 1 <= task_num <= len(tasks):
#                 removed = tasks.pop(task_num - 1)
#                 print(f"🗑 Task '{removed['title']}' removed!")
#             else:
#                 print("⚠ Invalid task number!")

#     # Mark task as done
#     elif choice == "4":
#         if not tasks:
#             print("⚠ No tasks to mark!")
#         else:
#             task_num = int(input("Enter task number to mark as done: "))
#             if 1 <= task_num <= len(tasks):
#                 tasks[task_num - 1]["done"] = True
#                 print(f"✔ Task '{tasks[task_num - 1]['title']}' marked as done!")
#             else:
#                 print("⚠ Invalid task number!")

#     # Exit the program
#     elif choice == "5":
#         print("👋 Exiting To-Do List... Goodbye!")
#         break

#     else:
#         print("⚠ Invalid choice! Please enter a number between 1-5.") 


# Student Information Management System
# Data stored in dictionaries and tuples

def print_menu():
    print("\n--- Student Information System ---")
    print("1. Add a new student")
    print("2. View student details")
    print("3. Exit")

def add_student(student_data):
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")

    # Store student details in a tuple (ID, Name, Grade)
    student_tuple = (student_id, name, grade)
    
    # Add to the dictionary (student_id -> student_tuple)
    student_data[student_id] = student_tuple
    print(f"Student {name} added successfully!")

def view_student(student_data):
    student_id = input("Enter student ID to view details: ")
    
    if student_id in student_data:
        student_tuple = student_data[student_id]
        print(f"Student ID: {student_tuple[0]}")
        print(f"Name: {student_tuple[1]}")
        print(f"Grade: {student_tuple[2]}")
    else:
        print("Student ID not found.")

def main():
    student_data = {}  # Dictionary to store student data

    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student(student_data)
        elif choice == '2':
            view_student(student_data)
        elif choice == '3':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main() 
