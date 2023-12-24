class Tasks:
    def __init__(self, desc, status):
        self.desc = desc
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, desc):
        tasks = Tasks(desc, "Incomplete")
        self.tasks.append(tasks)

    def complete_task(self, index):
        self.tasks[index].status = "Complete"

    def display_tasks(self):
        for index, tasks in enumerate(self.tasks):
            print(f"{index + 1}. {tasks.desc} - {tasks.status}")

todo_list = ToDoList()

while True:
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Display Tasks")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        desc = input("Enter task description: ")
        todo_list.add_task(desc)
    elif choice == "2":
        index = int(input("Enter task index to complete: ")) - 1
        todo_list.complete_task(index)
    elif choice == "3":
        todo_list.display_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
