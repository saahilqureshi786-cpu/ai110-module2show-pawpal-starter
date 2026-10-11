from datetime import date

import streamlit as st

from pawpal_system import Owner, Pet, Task, Scheduler


st.set_page_config(
    page_title="PawPal+",
    page_icon="🐾",
    layout="centered",
)

st.title("🐾 PawPal+")
st.write("Smart pet-care scheduling for multiple pets.")


# ---------------------------------------------------------
# Session state
# ---------------------------------------------------------

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Pet Owner")

owner = st.session_state.owner
scheduler = Scheduler(owner)


# ---------------------------------------------------------
# Owner
# ---------------------------------------------------------

st.header("👤 Owner")

owner_name = st.text_input(
    "Owner name",
    value=owner.name,
)

if st.button("Save owner"):
    if owner_name.strip():
        owner.name = owner_name.strip()
        st.success("Owner saved.")
    else:
        st.error("Owner name cannot be empty.")


# ---------------------------------------------------------
# Pets
# ---------------------------------------------------------

st.header("🐶 Pets")

with st.form("add_pet_form"):
    pet_name = st.text_input("Pet name")

    species = st.selectbox(
        "Species",
        ["Dog", "Cat", "Other"],
    )

    add_pet = st.form_submit_button("Add pet")

if add_pet:
    if not pet_name.strip():
        st.error("Pet name cannot be empty.")

    elif any(
        pet.name.lower() == pet_name.strip().lower()
        for pet in owner.pets
    ):
        st.error("A pet with that name already exists.")

    else:
        owner.add_pet(
            Pet(
                name=pet_name.strip(),
                species=species,
            )
        )

        st.success(f"{pet_name.strip()} added.")


if owner.pets:
    st.subheader("Current Pets")

    for pet in owner.pets:
        st.write(
            f"🐾 **{pet.name}** — {pet.species}"
        )

else:
    st.info("No pets added yet.")


# ---------------------------------------------------------
# Tasks
# ---------------------------------------------------------

st.header("📋 Add Care Task")

if owner.pets:

    pet_names = [
        pet.name
        for pet in owner.pets
    ]

    with st.form("add_task_form"):

        selected_pet_name = st.selectbox(
            "Pet",
            pet_names,
        )

        description = st.text_input(
            "Task description"
        )

        task_time = st.time_input(
            "Task time"
        )

        priority = st.selectbox(
            "Priority",
            ["low", "medium", "high"],
            index=1,
        )

        frequency = st.selectbox(
            "Frequency",
            ["once", "daily", "weekly"],
        )

        add_task = st.form_submit_button(
            "Add task"
        )

    if add_task:

        if not description.strip():

            st.error(
                "Task description cannot be empty."
            )

        else:

            selected_pet = next(
                pet
                for pet in owner.pets
                if pet.name == selected_pet_name
            )

            new_task = Task(
                description=description.strip(),
                time=task_time.strftime("%H:%M"),
                frequency=frequency,
                priority=priority,
                due_date=date.today(),
            )

            selected_pet.add_task(new_task)

            st.success(
                f"Task added for {selected_pet.name}."
            )

else:

    st.info(
        "Add a pet before creating tasks."
    )


# ---------------------------------------------------------
# Schedule
# ---------------------------------------------------------

st.header("📅 Today's Schedule")

tasks = scheduler.sort_by_time()

today_tasks = [
    (pet, task)
    for pet, task in tasks
    if task.due_date == date.today()
]

if today_tasks:

    schedule_rows = []

    for pet, task in today_tasks:

        schedule_rows.append(
            {
                "Time": task.time,
                "Pet": pet.name,
                "Task": task.description,
                "Priority": task.priority,
                "Frequency": task.frequency,
                "Completed": task.completed,
            }
        )

    st.table(schedule_rows)

else:

    st.info(
        "No tasks scheduled for today."
    )


# ---------------------------------------------------------
# Conflict detection
# ---------------------------------------------------------

st.header("⚠️ Conflict Detection")

conflicts = scheduler.detect_conflicts()

if conflicts:

    for pet1, task1, pet2, task2 in conflicts:

        st.warning(
            f"{pet1.name}'s '{task1.description}' "
            f"and {pet2.name}'s '{task2.description}' "
            f"are both scheduled at {task1.time}."
        )

else:

    st.success(
        "No scheduling conflicts detected."
    )


# ---------------------------------------------------------
# Reset
# ---------------------------------------------------------

st.divider()

if st.button("Reset PawPal+"):

    st.session_state.owner = Owner(
        "Pet Owner"
    )

    st.rerun()