# PawPal+

PawPal+ is a smart pet-care scheduling application built with Python, object-oriented programming, and Streamlit.

The system allows one owner to manage multiple pets and their care tasks. PawPal+ can organize tasks by time, filter tasks, detect scheduling conflicts, and automatically create the next occurrence of recurring tasks.

## Features

- Manage one owner and multiple pets
- Add pet-care tasks
- Sort tasks chronologically
- Filter tasks by pet or completion status
- Detect tasks scheduled at the same date and time
- Support one-time, daily, and weekly tasks
- Automatically create the next recurring task
- Display the schedule through a Streamlit interface
- Preserve app data during Streamlit reruns with `st.session_state`

## System Design

PawPal+ uses four main classes:

- **Owner** — stores owner information and manages multiple pets.
- **Pet** — stores pet information and its collection of tasks.
- **Task** — represents a care activity including time, priority, frequency, due date, and completion status.
- **Scheduler** — organizes tasks across all pets and provides sorting, filtering, conflict detection, and recurring-task behavior.

The Scheduler retrieves tasks through the Owner so that scheduling behavior works across multiple pets instead of only one pet.

## Smarter Scheduling

| Feature | Method | Behavior |
|---|---|---|
| Sorting | `Scheduler.sort_by_time()` | Sorts tasks by due date and time |
| Filtering | `Scheduler.filter_tasks()` | Filters by pet name or completion status |
| Conflict Detection | `Scheduler.detect_conflicts()` | Finds tasks scheduled at the same date and time |
| Recurring Tasks | `Scheduler.handle_recurring_task()` | Creates the next daily or weekly occurrence |

## Running PawPal+

Create and activate the virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the CLI demonstration:

```bash
python main.py
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Demo Walkthrough

1. Enter and save the owner's name.
2. Add pets such as Biscuit and Milo.
3. Add care tasks for each pet.
4. Choose the task time, priority, and recurrence frequency.
5. PawPal+ displays today's tasks in chronological order.
6. If two tasks share the same date and time, PawPal+ displays a conflict warning.
7. Recurring daily and weekly tasks can generate their next occurrence after completion.

## Sample CLI Output

```text
Today's Schedule
----------------
08:00 — Biscuit: Morning walk [high]
09:00 — Biscuit: Breakfast [high]
09:00 — Milo: Feeding [high]
10:00 — Milo: Medication [medium]

Biscuit's Tasks
----------------
2026-10-11 08:00 — Morning walk
2026-10-11 09:00 — Breakfast

Schedule Conflicts
------------------
WARNING: Biscuit's Breakfast and Milo's Feeding are both scheduled at 09:00.

Recurring Task Demo
-------------------
Completed: Morning walk on 2026-10-11
Next occurrence: Morning walk on 2026-10-12
```

## Testing PawPal+

Run the automated test suite with:

```bash
python -m pytest
```

The tests verify:

- Task completion
- Adding tasks to pets
- Chronological sorting
- Daily recurrence
- Conflict detection

Successful test result:

```text
5 passed
```

## Project Files

```text
app.py
pawpal_system.py
main.py
reflection.md
ai_interactions.md
requirements.txt
tests/test_pawpal.py
diagrams/uml_draft.mmd
diagrams/uml_final.mmd
```

## AI Collaboration

AI was used as a development assistant for system design, UML planning, code scaffolding, debugging, testing, and documentation.

AI suggestions were reviewed rather than accepted automatically. The implementation was verified using Python compilation, CLI demonstrations, Streamlit interaction, and automated pytest tests.