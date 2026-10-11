from dataclasses import dataclass, field


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "once"
    priority: str = "medium"
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self):
        """Return this pet's tasks."""
        return self.tasks


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        """Add a pet to the owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return all tasks across all pets."""
        all_tasks = []

        for pet in self.pets:
            for task in pet.get_tasks():
                all_tasks.append((pet, task))

        return all_tasks


class Scheduler:
    def __init__(self, owner):
        self.owner = owner

    def get_all_tasks(self):
        """Return all tasks across all pets."""
        return self.owner.get_all_tasks()

    def sort_by_time(self):
        """Return tasks sorted by time."""
        return sorted(
            self.owner.get_all_tasks(),
            key=lambda item: item[1].time,
        )

    def filter_tasks(self, pet_name=None, completed=None):
        """Filter tasks by pet name or completion status."""
        tasks = self.owner.get_all_tasks()

        if pet_name is not None:
            tasks = [
                (pet, task)
                for pet, task in tasks
                if pet.name.lower() == pet_name.lower()
            ]

        if completed is not None:
            tasks = [
                (pet, task)
                for pet, task in tasks
                if task.completed == completed
            ]

        return tasks

    def detect_conflicts(self):
        """Return tasks that share the same scheduled time."""
        tasks = self.owner.get_all_tasks()
        conflicts = []

        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                pet1, task1 = tasks[i]
                pet2, task2 = tasks[j]

                if task1.time == task2.time:
                    conflicts.append(
                        (pet1, task1, pet2, task2)
                    )

        return conflicts

    def handle_recurring_task(self):
        """Recurring-task logic will be added next."""
        pass