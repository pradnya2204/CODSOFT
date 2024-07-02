import datetime

class Task:
    def __init__(self, title, description, due_date, priority, tags):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.tags = tags
        self.status = "Not Started"
        self.created_at = datetime.datetime.now()

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due Date: {self.due_date}\n"
                f"Priority: {self.priority}\n"
                f"Tags: {', '.join(self.tags)}\n"
                f"Status: {self.status}\n"
                f"Created At: {self.created_at}\n")

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, title, **kwargs):
        task = self.find_task(title)
        if task:
            for key, value in kwargs.items():
                if hasattr(task, key):
                    setattr(task, key, value)

    def find_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def delete_task(self, title):
        task = self.find_task(title)
        if task:
            self.tasks.remove(task)

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def filter_tasks(self, **kwargs):
        filtered_tasks = self.tasks
        for key, value in kwargs.items():
            filtered_tasks = [task for task in filtered_tasks if getattr(task, key) == value]
        return filtered_tasks

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task\n2. Update Task\n3. Delete Task\n4. List Tasks\n5. Filter Tasks\n6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            priority = input("Priority (High, Medium, Low): ")
            tags = input("Tags (comma separated): ").split(",")
            task = Task(title, description, due_date, priority, tags)
            todo_list.add_task(task)
            print("Task added successfully.")

        elif choice == "2":
            title = input("Enter the title of the task to update: ")
            print("Leave blank if no change.")
            new_title = input("New Title: ")
            new_description = input("New Description: ")
            new_due_date = input("New Due Date (YYYY-MM-DD): ")
            new_priority = input("New Priority (High, Medium, Low): ")
            new_tags = input("New Tags (comma separated): ").split(",")

            kwargs = {}
            if new_title:
                kwargs["title"] = new_title
            if new_description:
                kwargs["description"] = new_description
            if new_due_date:
                kwargs["due_date"] = new_due_date
            if new_priority:
                kwargs["priority"] = new_priority
            if new_tags:
                kwargs["tags"] = new_tags

            todo_list.update_task(title, **kwargs)
            print("Task updated successfully.")

        elif choice == "3":
            title = input("Enter the title of the task to delete: ")
            todo_list.delete_task(title)
            print("Task deleted successfully.")

        elif choice == "4":
            todo_list.list_tasks()

        elif choice == "5":
            print("Filter options:")
            status = input("Status (Not Started, In Progress, Completed): ")
            priority = input("Priority (High, Medium, Low): ")
            tag = input("Tag: ")

            filters = {}
            if status:
                filters["status"] = status
            if priority:
                filters["priority"] = priority
            if tag:
                filters["tags"] = tag

            filtered_tasks = todo_list.filter_tasks(**filters)
            for task in filtered_tasks:
                print(task)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
