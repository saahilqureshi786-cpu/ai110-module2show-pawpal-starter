# PawPal+ — AI Interaction Log

## How I Used AI

I used ChatGPT as an AI coding assistant throughout the PawPal+ project.

The main areas where AI assisted were:

- OOP architecture planning
- UML design
- Python class scaffolding
- Scheduler algorithm development
- Debugging
- Automated test generation
- Streamlit integration
- README and reflection documentation

I reviewed and tested generated suggestions instead of assuming they were correct.

---

## System Design

### Prompt / Request

I asked AI to help design PawPal+ using four main classes:

- Owner
- Pet
- Task
- Scheduler

I also asked how the Scheduler should retrieve tasks across multiple pets rather than only one pet.

### AI Suggestion

AI suggested that:

- Owner should manage multiple Pet objects.
- Pet should manage its own Task objects.
- Task should contain care-task information.
- Scheduler should retrieve all tasks through the Owner.

### Final Decision

I accepted the overall structure.

The final relationship uses:

```python
Scheduler -> Owner -> Pets -> Tasks
```

This keeps the Scheduler responsible for scheduling while the Owner remains responsible for managing pets.

---

## UML and Class Scaffolding

### Prompt / Request

I asked AI to translate the class design into Mermaid UML and Python class skeletons.

### AI Suggestion

AI generated classes with attributes and methods for:

- Owner
- Pet
- Task
- Scheduler

It also suggested using Python dataclasses for Task and Pet.

### Final Decision

I used dataclasses for Task and Pet because they mainly store structured data.

Owner and Scheduler remain regular Python classes because they primarily coordinate other objects and behaviors.

---

## Scheduler Algorithms

### Prompt / Request

I asked AI for simple and readable implementations of:

- Sorting tasks chronologically
- Filtering tasks
- Detecting scheduling conflicts
- Handling recurring tasks

### Sorting

The final implementation uses Python's `sorted()` with task date and time as the key.

### Filtering

The Scheduler can filter tasks using:

- Pet name
- Completion status

### Conflict Detection

The implemented strategy checks whether two tasks have the exact same:

- Due date
- Time

If both match, they are reported as a conflict.

### Recurrence

Recurring tasks support:

- `daily` → next occurrence is one day later
- `weekly` → next occurrence is seven days later
- `once` → no new occurrence

Python's `timedelta` is used to calculate the next date.

---

## Debugging

AI was also used during debugging.

### Indentation Issue

While editing `Scheduler`, partial code replacements caused indentation errors.

Example error:

```text
IndentationError: unindent does not match any outer indentation level
```

To reduce editing mistakes, I changed my workflow and began replacing complete files instead of repeatedly inserting small fragments into existing code.

### Import Issue

At one point, `pawpal_system.py` accidentally contained:

```python
from pawpal_system import Owner, Pet, Task, Scheduler
```

This caused the file to import itself and produced an ImportError.

The incorrect import was removed from `pawpal_system.py` and kept only in `main.py`.

### Verification

After fixes, I verified the code with:

```bash
python -m py_compile pawpal_system.py
python main.py
```

---

## Testing

### Prompt / Request

I asked AI to create meaningful pytest tests for the most important PawPal+ behaviors.

### Tests Added

The final test suite verifies:

1. Task completion
2. Adding a task to a pet
3. Chronological task sorting
4. Daily recurring-task creation
5. Scheduling conflict detection

### Verification

I ran:

```bash
python -m pytest
```

Final result:

```text
5 passed
```

---

## Streamlit Integration

AI helped connect the Python backend to the Streamlit interface.

The final UI:

- Stores the Owner object in `st.session_state`
- Adds multiple pets
- Adds care tasks
- Displays the sorted daily schedule
- Shows conflict warnings
- Preserves data during Streamlit reruns

I manually tested the UI by adding Biscuit and Milo and scheduling tasks at the same time.

The conflict warning appeared correctly.

---

## Human Judgment

I did not accept every AI suggestion blindly.

One important change to my workflow happened after partial code edits repeatedly caused indentation and file-structure problems.

Instead of continuing to patch individual methods, I chose to use complete-file replacements and verify each change before moving forward.

I also used automated tests, CLI execution, compilation checks, and manual Streamlit testing to determine whether AI-generated code actually worked.

---

## Verification Methods

I used the following checks during development:

```bash
python -m py_compile pawpal_system.py
python main.py
python -m pytest
streamlit run app.py
```

These checks helped verify syntax, backend behavior, automated tests, and UI integration.

---

## Key Takeaway

AI was most useful for quickly generating designs, implementation ideas, tests, and debugging suggestions.

However, the project still required human decisions about architecture, correctness, readability, and whether AI-generated changes matched the project requirements.

My role was to use AI as an engineering assistant while remaining responsible for the final system.