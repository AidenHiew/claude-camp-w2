#Members Roster Manager (or a similar project tailored to your scenario)
#Storage: Use a dictionary to store member information (Name, Email, Join Date).
# Operations: Support three features: Add, Query (Search), and Delete.
# Interface: Command-line interface (CLI) where users type to select options.
# Error Handling: Provide user-friendly error prompts during invalid input; the application must not crash.

#Start by defining the main data structure to hold member information



Members = {}

#1 - Add New Member 
def add_members():
    name = input("Enter Member name: ")
    email = input("Enter member's email: ")
    join_date = input("Enter member's join date (DD-MM-YYYY): ")
    
    # Check if the member already exists in the dictionary
    if name in Members:
        print("Member already exists. Please use & add a different name.")
        return
    
    # Add the new member to the dictionary
    Members[name] = {
        'email': email,
        'join_date': join_date
    }
    print(f"Member {name} added successfully.")
    
    # Display the current list of members after adding a new member
    print("\n Current Members List:")
    for member_name, info in Members.items():
        print(f" - {member_name}: {info['email']} (Joined: {info['join_date']})")

    pass

#2 - Query Member Information
def query_member():
    name = input("Please enter the member's name to search:")
    if name in Members:
        print(f"Member {name} found in the list. Here are the details:")
        print(f"Member Name: {name}")
        print(f"Email: {Members[name]['email']}")
        print(f"Join Date: {Members[name]['join_date']}")
    else:
        print(f"Member {name} not found in the list.")
        

    pass


#3 - Delete Member
def delete_member():
    name = input("Please enter the member's name to remove:")
    if name in Members:
        del Members[name]
        print(f"Member {name} has been sucussfully removed.")
    else:
        print(f"Member {name} is not in the list. Cannot delete non-existing member.")

    pass


#4 - View All Members
def view_all_members():
    if not Members:
        print("No members are in the list yet.")
    else:
        print("Current Members List as below:")
        for member_name, info in Members.items():
            print(f" - {member_name}: {info['email']} (Joined: {info['join_date']})")


#5 - Exit the program
def exit_program():
    print("Thanks for using the Members Roster Manager. Exiting the program. Goodbye!")


def main():
    while True:
        print("\nWelcome to the Members Roster Manager!")
        print("Please select an option:")
        print("1. Add Member")
        print("2. Query Member")
        print("3. Delete Member")
        print("4. View All Members")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_members()
        elif choice == '2':
            query_member()
        elif choice == '3':
            delete_member()
        elif choice == '4':
            view_all_members()
        elif choice == '5':
            exit_program()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()


