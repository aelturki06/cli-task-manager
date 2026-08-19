class TaskNode:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.completed = False
        self.next = None


class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, title, priority):
        new_node = TaskNode(title, priority)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Task added: {title} ({priority})")

    def list_tasks(self):
        if self.head is None:
            print("No tasks yet.")
            return
        current = self.head
        index = 1
        while current:
            status = "Done" if current.completed else "Pending"
            print(f"{index}. [{current.priority}] {current.title} - {status}")
            current = current.next
            index += 1

    def complete_task(self, task_number):
        current = self.head
        index = 1
        while current:
            if index == task_number:
                current.completed = True
                print(f"Task {task_number} marked as complete.")
                return
            current = current.next
            index += 1
        print(f"Task {task_number} not found.")

    def delete_task(self, task_number):
        if self.head is None:
            print("No tasks to delete.")
            return

        if task_number == 1:
            self.head = self.head.next
            print(f"Task {task_number} deleted.")
            return

        current = self.head
        index = 1
        while current.next:
            if index + 1 == task_number:
                current.next = current.next.next
                print(f"Task {task_number} deleted.")
                return
            current = current.next
            index += 1

        print(f"Task {task_number} not found.")

    def sort_by_priority(self):
        priority_order = {"High": 1, "Medium": 2, "Low": 3}

        if self.head is None or self.head.next is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                current_rank = priority_order[current.priority]
                next_rank = priority_order[current.next.priority]
                if current_rank > next_rank:
                    current.title, current.next.title = current.next.title, current.title
                    current.priority, current.next.priority = current.next.priority, current.priority
                    current.completed, current.next.completed = current.next.completed, current.completed
                    swapped = True
                current = current.next

    def save_to_file(self, filename="tasks.txt"):
        with open(filename, "w") as f:
            current = self.head
            while current:
                f.write(f"{current.title}|{current.priority}|{current.completed}\n")
                current = current.next

    def load_from_file(self, filename="tasks.txt"):
        try:
            with open(filename, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    title, priority, completed = line.split("|")
                    self.add_task(title, priority)
                    if completed == "True":
                        current = self.head
                        while current.next:
                            current = current.next
                        current.completed = True
        except FileNotFoundError:
            pass


def main():
    tasks = TaskList()
    tasks.load_from_file()

    while True:
        print("\n===== Task Manager =====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Sort by priority")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            priority = input("Enter priority (High/Medium/Low):").strip().capitalize()
            if priority not in ("High", "Medium", "Low"):
                print("Invalid priority. Task not added.")
            else:
                tasks.add_task(title, priority)
                tasks.save_to_file()		

        elif choice == "2":
            tasks.list_tasks()

        elif choice == "3":
            tasks.list_tasks()
            task_number = int(input("Enter task number to complete: "))
            tasks.complete_task(task_number)
            tasks.save_to_file()

        elif choice == "4":
            tasks.list_tasks()
            task_number = int(input("Enter task number to delete: "))
            tasks.delete_task(task_number)
            tasks.save_to_file()

        elif choice == "5":
            tasks.sort_by_priority()
            tasks.list_tasks()
            tasks.save_to_file()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()