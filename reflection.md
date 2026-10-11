# PawPal+ Project Reflection

## 1. System Design

### a. Initial design

My initial design used four main classes:

- **Owner** — stores the owner's name, manages multiple pets, and handles JSON persistence.
- **Pet** — stores pet information and its collection of care tasks.
- **Task** — represents an individual care activity with a description, time, frequency, priority, completion status, and due date.
- **Scheduler** — retrieves and organizes tasks across all of the owner's pets.

The main relationships are:

- One Owner can have multiple Pets.
- Each Pet can have multiple Tasks.
- Scheduler works through Owner to retrieve tasks across all pets.

### b. Design changes

The design evolved during implementation.

I added `due_date` to Task so recurring tasks could distinguish today's occurrence from future occurrences.

I made Scheduler retrieve tasks through `Owner.get_all_tasks()` so sorting, filtering, conflict detection, priority scheduling, and next-available-slot logic work across multiple pets.

I also added JSON persistence through:

- `Owner.save_to_json()`
- `Owner.load_from_json()`

This allows pets and tasks to persist between application runs.

---

## 2. Scheduling Logic and Tradeoffs

The scheduler considers:

- Task time
- Due date
- Pet name
- Completion status
- Frequency
- Priority

Tasks can be sorted chronologically or by priority.

Priority scheduling follows:

```text
High → Medium → Low
```

Recurring tasks support:

- Daily → next day
- Weekly → seven days later
- Once → no new task

The `next_available_slot()` algorithm searches forward from a requested start time and checks tasks across all pets until it finds a free interval.

### Tradeoffs

The current conflict logic checks exact task start times.

For example, two tasks at 09:00 are considered a conflict. However, the system does not store task duration, so it cannot detect partial overlaps such as a 09:00–09:30 task conflicting with a task starting at 09:15.

A future version could add duration and true interval-overlap detection.

---

## 3. AI Collaboration

I used AI for:

- OOP architecture
- UML planning
- Python scaffolding
- Sorting and filtering
- Conflict detection
- Recurring tasks
- Priority scheduling
- JSON persistence
- Automated testing
- Streamlit integration
- Documentation
- Agent Mode implementation of `next_available_slot()`

I did not accept every AI suggestion automatically.

Partial code edits caused indentation and import problems, so I changed my workflow to use complete-file replacements for larger changes.

During Agent Mode, the agent attempted to use a different Python environment and then tried to install dependencies globally. I rejected that action because the project already had a working `.venv`.

I verified changes using:

```bash
python -m py_compile pawpal_system.py
python main.py
python -m pytest
streamlit run app.py
```

This reinforced that AI-generated work still requires human review and testing.

---

## 4. Testing and Verification

The final automated test suite verifies **8 behaviors**:

1. Task completion
2. Adding tasks to pets
3. Chronological sorting
4. Priority-based sorting
5. Daily recurrence
6. Multi-pet conflict detection
7. JSON persistence
8. Next available slot scheduling

The final test result is:

```text
8 passed
```

I also manually tested:

- Multiple pets
- Scheduling conflicts
- Streamlit UI behavior
- JSON persistence after restarting the application
- Priority-based schedule output

My confidence level is **5/5** for the implemented behaviors because all eight tests pass and both the CLI and Streamlit application work successfully.

Additional edge cases I would test in the future include:

- Pets with no tasks
- Owners with no pets
- Multiple simultaneous conflicts
- Weekly recurrence
- Invalid time inputs
- Next-slot searches near midnight
- True overlapping task durations
- Large numbers of pets and tasks

---

## 5. Reflection

### What went well

I am most satisfied with how PawPal+ evolved from a simple OOP design into a working multi-pet scheduling application.

The final system can:

- Manage multiple pets
- Sort tasks chronologically
- Sort tasks by priority
- Filter tasks
- Detect conflicts
- Create recurring tasks
- Find the next available scheduling slot
- Save and reload data using JSON
- Present information through a structured Streamlit interface

### What I would improve

In a future version, I would add:

- Task duration
- True overlapping-time conflict detection
- Task editing and deletion
- Stronger input validation
- More advanced automatic rescheduling

### Key takeaway

My main takeaway is that using AI effectively requires acting as the lead engineer rather than simply accepting generated code.

AI helped accelerate design, coding, debugging, testing, and documentation, but I still needed to make architectural decisions, reject inappropriate actions, verify correctness, and test the final system.

Good AI-assisted engineering still depends on clear requirements, modular design, meaningful testing, and human judgment.