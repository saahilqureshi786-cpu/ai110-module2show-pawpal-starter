from datetime import date, timedelta

from pawpal_system import Owner, Pet, Task, Scheduler


def test_task_completion():
    task = Task("Walk", "08:00")

    task.mark_complete()

    assert task.completed is True


def test_task_addition():
    pet = Pet("Biscuit", "Dog")
    task = Task("Breakfast", "09:00")

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0] == task


def test_sorting_correctness():
    owner = Owner("Saahil")

    dog = Pet("Biscuit", "Dog")
    cat = Pet("Milo", "Cat")

    owner.add_pet(dog)
    owner.add_pet(cat)

    today = date(2026, 10, 11)

    dog.add_task(
        Task(
            "Breakfast",
            "09:00",
            due_date=today,
        )
    )

    cat.add_task(
        Task(
            "Medication",
            "07:00",
            due_date=today,
        )
    )

    dog.add_task(
        Task(
            "Walk",
            "08:00",
            due_date=today,
        )
    )

    scheduler = Scheduler(owner)

    sorted_tasks = scheduler.sort_by_time()

    times = [
        task.time
        for pet, task in sorted_tasks
    ]

    assert times == [
        "07:00",
        "08:00",
        "09:00",
    ]


def test_daily_recurrence():
    owner = Owner("Saahil")
    pet = Pet("Biscuit", "Dog")
    owner.add_pet(pet)

    original_date = date(2026, 10, 11)

    task = Task(
        "Morning walk",
        "08:00",
        frequency="daily",
        due_date=original_date,
    )

    pet.add_task(task)

    scheduler = Scheduler(owner)

    next_task = scheduler.handle_recurring_task(
        pet,
        task,
    )

    assert task.completed is True
    assert next_task is not None
    assert next_task.due_date == (
        original_date + timedelta(days=1)
    )
    assert next_task.description == task.description
    assert next_task.completed is False


def test_conflict_detection():
    owner = Owner("Saahil")

    dog = Pet("Biscuit", "Dog")
    cat = Pet("Milo", "Cat")

    owner.add_pet(dog)
    owner.add_pet(cat)

    today = date(2026, 10, 11)

    dog.add_task(
        Task(
            "Breakfast",
            "09:00",
            due_date=today,
        )
    )

    cat.add_task(
        Task(
            "Feeding",
            "09:00",
            due_date=today,
        )
    )

    scheduler = Scheduler(owner)

    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1

    pet1, task1, pet2, task2 = conflicts[0]

    assert task1.time == task2.time
    assert task1.due_date == task2.due_date