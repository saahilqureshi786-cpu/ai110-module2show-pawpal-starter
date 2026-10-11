from datetime import date

from pawpal_system import Owner, Pet, Task, Scheduler


owner = Owner("Saahil")

biscuit = Pet("Biscuit", "Dog")
milo = Pet("Milo", "Cat")

owner.add_pet(biscuit)
owner.add_pet(milo)

today = date.today()

biscuit.add_task(
    Task(
        "Morning walk",
        "08:00",
        "daily",
        "medium",
        due_date=today,
    )
)

biscuit.add_task(
    Task(
        "Breakfast",
        "09:00",
        "daily",
        "high",
        due_date=today,
    )
)

milo.add_task(
    Task(
        "Medication",
        "10:00",
        "daily",
        "high",
        due_date=today,
    )
)

milo.add_task(
    Task(
        "Play time",
        "07:30",
        "once",
        "low",
        due_date=today,
    )
)

milo.add_task(
    Task(
        "Feeding",
        "09:00",
        "daily",
        "high",
        due_date=today,
    )
)

scheduler = Scheduler(owner)


print("Today's Schedule - Time Order")
print("-----------------------------")

for pet, task in scheduler.sort_by_time():
    if task.due_date == today:
        print(
            f"{task.time} — {pet.name}: "
            f"{task.description} [{task.priority}]"
        )


print("\nPriority Schedule")
print("-----------------")

for pet, task in scheduler.sort_by_priority():
    if task.due_date == today:
        print(
            f"[{task.priority.upper()}] "
            f"{task.time} — {pet.name}: "
            f"{task.description}"
        )


print("\nBiscuit's Tasks")
print("----------------")

for pet, task in scheduler.filter_tasks(
    pet_name="Biscuit"
):
    print(
        f"{task.due_date} {task.time} — "
        f"{task.description}"
    )


print("\nSchedule Conflicts")
print("------------------")

conflicts = scheduler.detect_conflicts()

if conflicts:
    for pet1, task1, pet2, task2 in conflicts:
        print(
            f"WARNING: {pet1.name}'s "
            f"{task1.description} and "
            f"{pet2.name}'s {task2.description} "
            f"are both scheduled at {task1.time}."
        )
else:
    print("No conflicts found.")


print("\nRecurring Task Demo")
print("-------------------")

morning_walk = biscuit.tasks[0]

next_walk = scheduler.handle_recurring_task(
    biscuit,
    morning_walk,
)

print(
    f"Completed: {morning_walk.description} "
    f"on {morning_walk.due_date}"
)

if next_walk:
    print(
        f"Next occurrence: {next_walk.description} "
        f"on {next_walk.due_date}"
    )

print("\nNext Available Slot Demo")
print("------------------------")

slot = scheduler.next_available_slot(
    today,
    "09:00",
    30,
)

print(
    f"Next free 30-minute slot starting at "
    f"{slot} on {today}"
)