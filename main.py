from pawpal_system import Owner, Pet, Task, Scheduler


owner = Owner("Saahil")

biscuit = Pet("Biscuit", "Dog")
milo = Pet("Milo", "Cat")

owner.add_pet(biscuit)
owner.add_pet(milo)

biscuit.add_task(
    Task("Morning walk", "08:00", "daily", "high")
)

biscuit.add_task(
    Task("Breakfast", "09:00", "daily", "high")
)

milo.add_task(
    Task("Medication", "10:00", "daily", "medium")
)

milo.add_task(
    Task("Feeding", "09:00", "daily", "high")
)

scheduler = Scheduler(owner)


print("Today's Schedule")
print("----------------")

for pet, task in scheduler.sort_by_time():
    print(
        f"{task.time} — {pet.name}: "
        f"{task.description} [{task.priority}]"
    )


print("\nBiscuit's Tasks")
print("----------------")

for pet, task in scheduler.filter_tasks(
    pet_name="Biscuit"
):
    print(f"{task.time} — {task.description}")


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