"""
Engineering Task & Sprint Scheduler
-----------------------------------
A lightweight command-line project management application built with Python.
Designed to handle dynamic memory allocation for project sprints utilizing nested
data structures (lists and dictionaries).

Features:
- Dynamic Task Creation with ID tracking and priority constraints.
- Real-time Board State updates (Movements between Todo, Doing, Done).
- Context-aware filtering based on priority matrix.

Author: Software Engineering Student
Date: July 2026
"""
def create_task(project_board, task_counter):
    title = input("Enter the title: ")
    priority = int(input("Enter the priority(1-3): "))
    if priority not in range(1,4):
        print("Invalid priority, please enter a priority between 1 and 3")
        return task_counter
    else:
        task = {
            "id": task_counter,
            "title": title,
            "priority": priority
        }
        project_board["Todo"].append(task)
        return task_counter + 1
def update_task_status(project_board):
    found = False
    task_id = int(input("Enter the ID of the task that you want to update: "))
    for status in project_board:
        for task in project_board[status]:
            if task['id'] == task_id:
                found = True
                user = input("Enter the new status (Doing/Done): ")
                if user in  ["Todo", "Doing", "Done"]:
                   project_board[status].remove(task)
                   project_board[user].append(task)
                   print(f"Task '{task['title']}' moved to {user} successfully.")
                if not found:
                    print("Invalid status, please enter either Doing or Done")
                return project_board
def view_project_board(project_board):
    for i in project_board.keys():
        if len(project_board[i]) == 0:
            print("Empty")
        else:
            for task in project_board[i]:
                print(f"[ID: {task['id']}, Title: {task['title']}, Priority: {task['priority']}]")
def view_high_priority_task(project_board):
     has_high = False
     for y in project_board:
         for k in project_board[y]:
             if k['priority'] == 1:
                 has_high = True
                 print(f"[ID: {k['id']}, Title: {k['title']}, Priority: {k['priority']}]")
             if not has_high:
                 print("No high priority tasks found.")
def main_menu():
    project_board = {
        "Todo" : [],
        "Doing" : [],
        "Done" : []
    }
    task_counter = 1
    while True:
        print("\n ===== Engineering Task Scheduler =====")
        print("1. Create new task")
        print("2. Update task ststus")
        print("3. View project board")
        print("4. View high priority")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task_counter = create_task(project_board, task_counter)
        elif choice == "2":
             update_task_status(project_board)
        elif choice == "3":
             view_project_board(project_board)
        elif choice == "4":
            view_high_priority_task(project_board)
        elif choice == "5":
            print("Goodbye")
        else:
            print("Invalid choice, please try again.")
main_menu()