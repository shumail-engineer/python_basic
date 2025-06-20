# To-Do List App

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def main():
    tasks = []

    print("Welcome to the To-Do List App!")

    while True:
        print("\nChoose an option:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter a new task: ")
            tasks.append(task)
            print("Task added!")
        elif choice == "2":
            print("\nYour Tasks:")
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
