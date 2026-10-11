# PawPal+ Project Reflection

## 1. System Design

### a. Initial design

My initial design used four main classes:

- **Owner** — stores the owner's name and manages multiple pets.
- **Pet** — stores pet information and its collection of care tasks.
- **Task** — represents an individual care activity with a description, time, frequency, priority, completion status, and due date.
- **Scheduler** — acts as the scheduling layer that retrieves and organizes tasks across all of the owner's pets.

The three main user actions I designed for were:

1. Add and manage pets.
2. Add care tasks such as walks, feeding, medication, and appointments.
3. View an organized daily schedule with sorting, filtering, recurring tasks, and conflict warnings.

The main relationships are that one Owner can have multiple Pets, each Pet can have multiple Tasks, and the Scheduler works through the Owner to retrieve tasks across all pets.

### b. Design changes

The design changed as the implementation became more complete.

Initially, Task only needed a description, time, frequency, priority, and completion status. I later added a `due_date` attribute because recurring tasks needed a way to distinguish today's occurrence from the next daily or weekly occurrence.

I also made the Scheduler retrieve tasks through `Owner.get_all_tasks()` instead of directly accessing one pet. This keeps the scheduling logic multi-pet and allows sorting, filtering, and conflict detection to work across the entire owner's schedule.

---

## 2. Scheduling Logic and Tradeoffs

### a. Constraints and priorities

The scheduler considers several pieces of information:

- Task time
- Due date
- Pet name
- Completion status
- Frequency
- Priority

Tasks are sorted chronologically using the due date and time. Filtering can narrow results by pet name or completion status.

Recurring tasks use their frequency to decide when the next task should be created:

- Daily → next day
- Weekly → seven days later
- Once → no new task

I focused first on time and date because those directly affect the order of the daily schedule and whether two tasks conflict.

### b. Tradeoffs

One tradeoff in the current conflict-detection algorithm is that it only checks for tasks with the exact same date and exact same time.

For example, two tasks both scheduled at 09:00 are considered a conflict. However, the system does not currently consider task duration, so a task from 09:00–09:30 would not conflict with another task beginning at 09:15.

I chose this simpler approach because it is easy to understand, predictable, and sufficient for the project's basic scheduling requirements. A future version could store task duration and detect overlapping time ranges.

---

## 3. AI Collaboration

### a. How I used AI

I used AI throughout the project for:

- Brainstorming the OOP architecture
- Creating the initial UML structure
- Scaffolding the Python classes
- Implementing sorting, filtering, conflict detection, and recurring-task logic
- Debugging indentation and import errors
- Designing pytest cases
- Connecting the backend classes to Streamlit
- Improving documentation and README structure

The most useful prompts were specific requests that included the current code and the exact behavior I wanted to verify.

For example, asking how the Scheduler should retrieve tasks across multiple pets helped establish the relationship between `Scheduler` and `Owner.get_all_tasks()`.

### b. Judgment and verification

I did not accept every AI suggestion as-is.

During implementation, some partial code edits caused indentation problems and at one point resulted in an incorrect self-import inside `pawpal_system.py`. Instead of continuing with small patches, I changed the workflow and used complete-file replacements so that I could verify the full structure consistently.

I verified AI-generated code using several methods:

- `python -m py_compile pawpal_system.py` for syntax
- `python main.py` for end-to-end CLI behavior
- `python -m pytest` for automated testing
- `streamlit run app.py` for UI integration
- Manual testing of two tasks scheduled at the same time to confirm conflict warnings

This showed me that AI output still needs human review and testing before it should be trusted.

---

## 4. Testing and Verification

### a. What I tested

The automated test suite verifies five behaviors:

1. A task changes to completed after `mark_complete()`.
2. Adding a task to a Pet increases its task collection.
3. Scheduler sorting returns tasks in chronological order.
4. Completing a daily recurring task creates a new task for the following day.
5. The Scheduler detects two tasks scheduled for the same date and time.

These tests were important because they cover both the basic object behavior and the main scheduling algorithms.

I also manually tested the Streamlit interface by adding multiple pets and creating tasks with duplicate times to verify that conflict warnings appear correctly.

### b. Confidence

My confidence level is **5/5** for the behaviors currently implemented because all five automated tests pass and the CLI and Streamlit demonstrations work successfully.

If I had more time, I would test additional edge cases such as:

- A pet with no tasks
- An owner with no pets
- Multiple conflicts at the same time
- Weekly recurrence
- Invalid time values
- Duplicate pet names
- Tasks spanning overlapping time ranges rather than exact matches
- Large numbers of pets and tasks

---

## 5. Reflection

### a. What went well

I am most satisfied with the way the system evolved from a simple UML design into a working multi-pet scheduling application.

The Scheduler can now organize tasks across multiple pets, sort them chronologically, filter them, identify conflicts, and create future recurring tasks. The same backend logic is also connected to both a CLI demonstration and a Streamlit interface.

### b. What I would improve

With another iteration, I would improve the scheduling model by adding task duration and true overlapping-time conflict detection.

I would also add persistent storage so pets and tasks remain available after the Streamlit application is closed. Right now, `st.session_state` preserves data during the active Streamlit session, but not between separate application runs.

Another improvement would be priority-based scheduling where high-priority tasks are considered alongside time when generating the daily plan.

### c. Key takeaway

My main takeaway is that using AI effectively requires acting as the lead architect rather than simply accepting generated code.

AI was useful for brainstorming, scaffolding, debugging, and testing, but I still needed to decide the system structure, verify whether suggestions matched the project requirements, identify errors, and test the final behavior.

The most important lesson was that good AI-assisted engineering still depends on clear requirements, modular design, meaningful tests, and human judgment.