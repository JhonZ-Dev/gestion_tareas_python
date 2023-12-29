import os
import pickle

class TaskManager:
    def __init__(self, filename="tasks.pkl"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.tasks, file)
    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f'Tarea "{task}" añadida con éxito.')
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.save_tasks()
            print(f'Tarea "{task}" eliminada con éxito.')
        else:
            print(f'Tarea "{task}" no encontrada.')

    def list_tasks(self):
        if not self.tasks:
            print("No hay tareas.")
        else:
            print("Lista de tareas:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
def main():
    task_manager = TaskManager()

