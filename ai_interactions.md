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
- Data persistence
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

```text
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

I asked AI for readable implementations of:

- Sorting tasks chronologically
- Filtering tasks
- Detecting scheduling conflicts
- Handling recurring tasks
- Priority-based scheduling

### Sorting

The final implementation uses Python's `sorted()` with task date and time as the key.

### Priority Scheduling

The advanced scheduler uses a priority map:

```text
high -> 0
medium -> 1
low -> 2
```

Tasks are sorted by priority first, followed by due date and time.

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

## Data Persistence

### Prompt / Request

I asked AI to add JSON persistence so PawPal+ could remember pets and tasks between application runs.

### Implementation

The Owner class now provides:

```python
save_to_json()
load_from_json()
```

Task dates are converted to ISO-formatted strings when saved and reconstructed as Python `date` objects when loaded.

The Streamlit application automatically loads `data.json` when it starts and saves changes after owner, pet, or task updates.

### Verification

I tested persistence by:

1. Adding a pet and task in Streamlit.
2. Stopping the Streamlit server.
3. Starting the app again.
4. Confirming that the saved pet and task were still available.

I also added an automated pytest persistence test.

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

The test suite verifies:

1. Task completion
2. Adding a task to a pet
3. Chronological task sorting
4. Priority-based scheduling
5. Daily recurring-task creation
6. Scheduling conflict detection
7. JSON data persistence

### Verification

I ran:

```bash
python -m pytest
```

Final result:

```text
7 passed
```

---

## Streamlit Integration

AI helped connect the Python backend to the Streamlit interface.

The final UI:

- Stores the Owner object in `st.session_state`
- Adds multiple pets
- Adds care tasks
- Displays the sorted daily schedule
- Displays a priority-based schedule
- Shows conflict warnings
- Uses dashboard metrics and status indicators
- Saves data to JSON
- Restores saved data when the application restarts

I manually tested the UI by adding Biscuit and Milo and scheduling tasks at the same time.

The conflict warning appeared correctly.

---

## Prompt Strategy Comparison

### Strategy 1 — Incremental / Partial Code Edits

**Model / Tool:** ChatGPT

**Prompting strategy:**  
Ask AI to provide only the small method or code block that needed to change.

**Task:**  
Implement individual Scheduler methods such as `sort_by_time()`, `filter_tasks()`, and `detect_conflicts()`.

**What was useful:**

- Responses were short.
- It was easy to focus on one concept at a time.
- Individual algorithms were easier to understand.

**Problems:**

- Copying small blocks into an existing class caused indentation mistakes.
- Some old code remained in the file.
- One edit resulted in an incorrect self-import.
- Debugging took additional time because the full file structure was not always visible.

### Strategy 2 — Complete-File Replacement

**Model / Tool:** ChatGPT

**Prompting strategy:**  
Provide the entire updated file whenever a significant change is required.

**Task:**  
Repair and extend `pawpal_system.py`, `main.py`, `app.py`, and the test suite while preserving the complete file structure.

**What was useful:**

- Indentation was much more consistent.
- Imports and class relationships were easier to verify.
- It reduced the chance of leaving obsolete code behind.
- It was faster to copy, save, run, and test.
- The full context made later changes easier to reason about.

**Problems:**

- Responses were longer.
- I still had to review the entire file before replacing my existing code.
- A full-file replacement can overwrite manual changes if it is used carelessly.

### Final Decision

For PawPal+, I preferred the **complete-file replacement strategy** for larger structural changes because it reduced integration errors and made verification faster.

For very small changes, an incremental edit can still be useful, but only when the exact insertion point is clear.

This comparison changed how I worked with AI during the project. Instead of treating generated code as isolated snippets, I began considering how each suggestion fit into the complete application.

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

These checks helped verify syntax, backend behavior, automated tests, persistence, and UI integration.

---

## Key Takeaway

AI was most useful for quickly generating designs, implementation ideas, tests, and debugging suggestions.

However, the project still required human decisions about architecture, correctness, readability, and whether AI-generated changes matched the project requirements.

My role was to use AI as an engineering assistant while remaining responsible for the final system.