# PawPal+

PawPal+ is a smart multi-pet care scheduling application built with Python, object-oriented programming, pytest, JSON persistence, and Streamlit.

The system allows one owner to manage multiple pets and their care tasks. PawPal+ can organize tasks by time and priority, filter tasks, detect scheduling conflicts, generate recurring tasks, find the next available care slot, and preserve data between application runs.

## Features

- Manage one owner and multiple pets
- Add pet-care tasks
- Sort tasks chronologically
- Sort tasks by priority
- Filter tasks by pet or completion status
- Detect tasks scheduled at the same date and time
- Support one-time, daily, and weekly tasks
- Automatically create the next recurring task
- Find the next available scheduling slot
- Save and restore pets/tasks using JSON
- Display a structured Streamlit dashboard
- Show pet, task, conflict, and completion metrics
- Use tables, emojis, priority indicators, and status messages

## System Design

PawPal+ uses four main classes:

- **Owner** — stores owner information, manages multiple pets, and handles JSON persistence.
- **Pet** — stores pet information and its collection of tasks.
- **Task** — represents a care activity including description, time, priority, frequency, due date, and completion status.
- **Scheduler** — organizes tasks across all pets and provides scheduling algorithms.

The primary relationship is:

```text
Scheduler -> Owner -> Pets -> Tasks
```

The Scheduler retrieves tasks through the Owner so scheduling behavior works across all pets.

## Scheduling Algorithms

| Feature | Method | Behavior |
|---|---|---|
| Chronological Sorting | `Scheduler.sort_by_time()` | Sorts by due date and time |
| Priority Scheduling | `Scheduler.sort_by_priority()` | Sorts High → Medium → Low, then date/time |
| Filtering | `Scheduler.filter_tasks()` | Filters by pet or completion status |
| Conflict Detection | `Scheduler.detect_conflicts()` | Finds tasks with the same date and time |
| Recurring Tasks | `Scheduler.handle_recurring_task()` | Creates the next daily or weekly occurrence |
| Next Available Slot | `Scheduler.next_available_slot()` | Searches forward for the next free scheduling interval |

## Advanced Algorithm: Next Available Slot

The `next_available_slot()` algorithm works across tasks belonging to all pets.

It accepts:

- a target date
- a starting time
- an interval length in minutes

The Scheduler checks each candidate interval against existing tasks. If a conflict exists, it moves forward by the requested interval until it finds an available slot.

Example:

```text
Existing tasks:
09:00 — Breakfast
09:30 — Feeding

Requested:
Start = 09:00
Interval = 30 minutes

Result:
10:00
```

This feature was implemented using Agent Mode and verified with an automated pytest case and a CLI demonstration.

## Advanced Scheduling: Priority Sorting

PawPal+ includes priority-based scheduling.

Priority values are ranked as:

```text
HIGH
MEDIUM
LOW
```

When priorities are equal, tasks are ordered by due date and time.

Example CLI output:

```text
Priority Schedule
-----------------
[HIGH] 09:00 — Biscuit: Breakfast
[HIGH] 09:00 — Milo: Feeding
[HIGH] 10:00 — Milo: Medication
[MEDIUM] 08:00 — Biscuit: Morning walk
[LOW] 07:30 — Milo: Play time
```

## JSON Data Persistence

PawPal+ saves application data between runs using JSON.

Persistence methods are implemented in `Owner`:

```python
save_to_json()
load_from_json()
```

The Streamlit application:

1. Checks whether `data.json` exists.
2. Loads the saved Owner, Pets, and Tasks when the app starts.
3. Saves data whenever the owner, a pet, or a task is updated.
4. Reconstructs saved ISO date strings as Python `date` objects.

The runtime `data.json` file is excluded from Git with `.gitignore`.

Persistence-related files:

```text
pawpal_system.py
app.py
tests/test_pawpal.py
.gitignore
```

## Professional Streamlit UI

The Streamlit interface uses structured formatting to make the care schedule easier to understand.

Formatting features include:

- `st.columns()` for dashboard layout
- `st.metric()` for pet, task, conflict, and completion counts
- `st.table()` for structured schedules
- `st.success()` for successful actions
- `st.warning()` for scheduling conflicts
- `st.error()` for invalid input and conflict summaries
- Emoji-based task, priority, frequency, and completion indicators

Examples:

```text
🔴 High
🟡 Medium
🟢 Low

✅ Complete
⏳ Pending

🔁 Daily
📆 Weekly
```

## Running PawPal+

Create the virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
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

## CLI Demonstration

Example output:

```text
Today's Schedule - Time Order
-----------------------------
07:30 — Milo: Play time [low]
08:00 — Biscuit: Morning walk [medium]
09:00 — Biscuit: Breakfast [high]
09:00 — Milo: Feeding [high]
10:00 — Milo: Medication [high]

Priority Schedule
-----------------
[HIGH] 09:00 — Biscuit: Breakfast
[HIGH] 09:00 — Milo: Feeding
[HIGH] 10:00 — Milo: Medication
[MEDIUM] 08:00 — Biscuit: Morning walk
[LOW] 07:30 — Milo: Play time

Schedule Conflicts
------------------
WARNING: Biscuit's Breakfast and Milo's Feeding are both scheduled at 09:00.

Recurring Task Demo
-------------------
Completed: Morning walk on 2026-10-11
Next occurrence: Morning walk on 2026-10-12

Next Available Slot Demo
------------------------
Next free 30-minute slot starting at 09:30 on 2026-10-11
```

## Testing

Run all tests with:

```bash
python -m pytest
```

The automated suite verifies:

1. Task completion
2. Adding tasks to pets
3. Chronological sorting
4. Priority-based sorting
5. Daily recurrence
6. Multi-pet conflict detection
7. JSON persistence
8. Next available slot scheduling

Passing test result:

```text
8 passed
```

## AI Collaboration

AI was used as an engineering assistant for:

- System design
- UML planning
- Python scaffolding
- Scheduling algorithms
- Debugging
- Test generation
- Streamlit integration
- JSON persistence
- Agent Mode feature implementation
- Documentation

AI output was not accepted automatically.

All significant changes were verified using:

```bash
python -m py_compile pawpal_system.py
python main.py
python -m pytest
streamlit run app.py
```

The full AI development workflow and prompt-strategy comparison are documented in `ai_interactions.md`.

## Project Files

```text
app.py
pawpal_system.py
main.py
reflection.md
ai_interactions.md
requirements.txt
.gitignore
tests/test_pawpal.py
diagrams/uml_draft.mmd
diagrams/uml_final.mmd
```