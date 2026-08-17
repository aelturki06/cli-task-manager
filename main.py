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


if __name__ == "__main__":
    tasks = TaskList()
    tasks.add_task("Finish CV", "High")
    tasks.add_task("Buy groceries", "Low")
    tasks.add_task("Clean house", "Medium")
    tasks.add_task("Call bank", "High")
    tasks.list_tasks()

    print("\n--- Sorting by priority ---")
    tasks.sort_by_priority()
    tasks.list_tasks()

