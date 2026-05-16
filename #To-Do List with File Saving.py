#To-Do List with File Saving
#Build a to-do list program with the following features:
#Add a to-do item
#Mark a to-do item as completed
#View the to-do list
#The program should also:
#Save the data to a local todos.json file
#Load previous data after the program restarts
#Avoid errors if the file does not exist
#This is a practical use case for exception handling


import json

FILE_NAME = "todolist.json"
def load_todolist():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    pass

#save current to-do list to file

def save_todolist(todolist):
    with open(FILE_NAME, 'w') as file:
        json.dump(todolist, file, indent=4)

#view the to-do list with status indicators

def view_todolist(todolist):
    if not todolist:
        print("\nYour to-do list is empty.")
    else:
        for index, item in enumerate(todolist, start=1):
            status = "✓" if item['completed'] else "✗"
            print(f"{index}. [{status}] {item['task']}")

#add a new to-do item

def add_todolist(todolist):
    task  = input("\nEnter a new to-do item of your choice:")
    if task.strip() =="":
        print("Task cannot be empty. Please try again.")
        return
    
    new_todo = {
        "task": task,
        "completed": False
    }
    todolist.append(new_todo)
    save_todolist(todolist)
    print("To-do item added successfully.")

#mark a to-do item as completed

def mark_completed(todolist):
    view_todolist(todolist)
    try:
        index = int(input("\nEnter the number of the to-do item to mark as completed: ")) - 1
        if 0 <= index < len(todolist):
            todolist[index]['completed'] = True
            save_todolist(todolist)
            print("To-do item marked as completed.")
        else:
            print("Invalid index. Please try again.")
    except ValueError:
        print("Please enter a valid number.")


def show_menu():
    #display menu and handle user input
    print("\n ---- To-Do List App ----")
    print("1. View All To-Do List")
    print("2. Add New To-Do Item")
    print("3. Mark To-Do Item as Completed")
    print("4. Exit the program")

def main():
    todolist = load_todolist()
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            view_todolist(todolist)
        elif choice == '2':
            add_todolist(todolist)
        elif choice == '3':
            mark_completed(todolist)
        elif choice == '4':
            print("Thank you for using the APP, Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

main()