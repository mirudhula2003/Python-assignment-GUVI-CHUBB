import pickle

def save_tasks(task_list, filename='tasks.pkl'):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(task_list, file)
        print("Tasks saved!")
    except Exception as e:
        print("Error in saving tasks", e)

def load_tasks(filename='tasks.pkl'):
    try:
        with open(filename, 'rb') as file:
            tasks = pickle.load(file)
        print("Tasks loaded successfully!")
        return tasks
    except FileNotFoundError:
        print("No tasks found.")
        return []
    except (pickle.UnpicklingError, EOFError):
        print("File corrupted")
        return []

tasks = ["Buy groceries", "Call the plumber", "Finish the project"]

save_tasks(tasks)
retrieved_tasks = load_tasks()
print("current tasks:", retrieved_tasks)

