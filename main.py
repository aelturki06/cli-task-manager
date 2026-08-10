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


if __name__ == "__main__":
    tasks = TaskList()
    tasks.add_task("Finish CV", "High")
    tasks.add_task("Buy groceries", "Low")
    tasks.list_tasks()