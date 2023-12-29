import os
import pickle

class TaskManager:
    def __init__(self, filename="tasks.pkl"):
        self.filename = filename
        self.tasks = self.load_tasks()