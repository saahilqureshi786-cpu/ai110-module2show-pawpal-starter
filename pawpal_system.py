import json
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "once"
    priority: str = "medium"
    completed: bool = False
    due_date: date = field(default_factory=date.today)

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

    def save_to_json(self, file_path="data.json"):
        """Save the owner, pets, and tasks to JSON."""
        data = {
            "name": self.name,
            "pets": [],
        }

        for pet in self.pets:
            pet_data = {
                "name": pet.name,
                "species": pet.species,
                "tasks": [],
            }

            for task in pet.tasks:
                pet_data["tasks"].append(
                    {
                        "description": task.description,
                        "time": task.time,
                        "frequency": task.frequency,
                        "priority": task.priority,
                        "completed": task.completed,
                        "due_date": task.due_date.isoformat(),
                    }
                )

            data["pets"].append(pet_data)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

    @classmethod
    def load_from_json(cls, file_path="data.json"):
        """Load an owner, pets, and tasks from JSON."""
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        owner = cls(data["name"])

        for pet_data in data.get("pets", []):
            pet = Pet(
                name=pet_data["name"],
                species=pet_data["species"],
            )

            for task_data in pet_data.get("tasks", []):
                task = Task(
                    description=task_data["description"],
                    time=task_data["time"],
                    frequency=task_data["frequency"],
                    priority=task_data["priority"],
                    completed=task_data["completed"],
                    due_date=date.fromisoformat(
                        task_data["due_date"]
                    ),
                )

                pet.add_task(task)

            owner.add_pet(pet)

        return owner


class Scheduler:
    def __init__(self, owner):
        self.owner = owner

    def get_all_tasks(self):
        """Return all tasks across all pets."""
        return self.owner.get_all_tasks()

    def sort_by_time(self):
        """Return tasks sorted by date and time."""
        return sorted(
            self.owner.get_all_tasks(),
            key=lambda item: (
                item[1].due_date,
                item[1].time,
            ),
        )

    def sort_by_priority(self):
        """Return tasks sorted by priority, then date and time."""
        priority_order = {
            "high": 0,
            "medium": 1,
            "low": 2,
        }

        return sorted(
            self.owner.get_all_tasks(),
            key=lambda item: (
                priority_order.get(
                    item[1].priority.lower(),
                    3,
                ),
                item[1].due_date,
                item[1].time,
            ),
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
        """Return tasks scheduled for the same date and time."""
        tasks = self.owner.get_all_tasks()
        conflicts = []

        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                pet1, task1 = tasks[i]
                pet2, task2 = tasks[j]

                same_date = task1.due_date == task2.due_date
                same_time = task1.time == task2.time

                if same_date and same_time:
                    conflicts.append(
                        (pet1, task1, pet2, task2)
                    )

        return conflicts

    def next_available_slot(self, target_date, start_time, interval_minutes):
        """Return the next free time slot on the given date."""
        if interval_minutes <= 0:
            raise ValueError("interval_minutes must be greater than 0")

        candidate = datetime.strptime(
            f"{target_date.isoformat()} {start_time}",
            "%Y-%m-%d %H:%M",
        )

        while candidate.date() == target_date:
            slot_end = candidate + timedelta(minutes=interval_minutes)
            conflict = False

            for pet, task in self.owner.get_all_tasks():
                if task.due_date != target_date:
                    continue

                task_start = datetime.strptime(
                    f"{task.due_date.isoformat()} {task.time}",
                    "%Y-%m-%d %H:%M",
                )

                if task_start >= candidate and task_start < slot_end:
                    conflict = True
                    break

            if not conflict:
                return candidate.strftime("%H:%M")

            candidate += timedelta(minutes=interval_minutes)

        return None

    def handle_recurring_task(self, pet, task):
        """Complete a task and create its next recurring occurrence."""
        task.mark_complete()

        frequency = task.frequency.lower()

        if frequency == "daily":
            next_date = task.due_date + timedelta(days=1)

        elif frequency == "weekly":
            next_date = task.due_date + timedelta(days=7)

        else:
            return None

        next_task = Task(
            description=task.description,
            time=task.time,
            frequency=task.frequency,
            priority=task.priority,
            completed=False,
            due_date=next_date,
        )

        pet.add_task(next_task)

        return next_task