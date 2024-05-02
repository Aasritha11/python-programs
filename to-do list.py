
def main():
    """
    Main function to manage the to-do list application.
    """

    tasks = []

    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Done")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please try again.")


def add_task(tasks):
    """
    Prompts the user for a new task and adds it to the to-do list.
    """

    new_task = input("Enter new task: ")
    tasks.append(new_task)
    print(f"Task '{new_task}' added successfully!")


def view_tasks(tasks):
    """
    Displays the current to-do list.
    """

    if not tasks:
        print("There are no tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def mark_task_done(tasks):
    """
    Allows the user to mark a task as completed and removes it from the list.
    """

    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("Enter the number of the task to mark as done: "))
        task_index = task_number - 1
        tasks.pop(task_index)
        print("Task marked done successfully!")
    except (IndexError, ValueError):
        print("Invalid task number. Please try again.")


def remove_task(tasks):
    """
    Enables the user to remove a task by its number.
    """

    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("Enter the number of the task to remove: "))
        task_index = task_number - 1
        tasks.pop(task_index)
        print("Task removed successfully!")
    except (IndexError, ValueError):
        print("Invalid task number. Please try again.")


if __name__ == "__main__":
    main()
