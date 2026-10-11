# PawPal+ — AI Interaction Log

## How I Used AI

I used ChatGPT and an AI coding Agent as engineering assistants throughout the PawPal+ project.

AI assisted with:

- OOP architecture planning
- UML design
- Python class scaffolding
- Scheduling algorithm development
- Debugging
- Automated test generation
- Streamlit integration
- JSON persistence
- Advanced scheduling
- Documentation

I reviewed and tested generated suggestions rather than assuming they were correct.

---

## System Design

### Task

Design PawPal+ using four core classes:

- Owner
- Pet
- Task
- Scheduler

The Scheduler needed to operate across multiple pets.

### AI Suggestion

AI suggested this relationship:

```text
Scheduler -> Owner -> Pets -> Tasks
```

Owner manages Pet objects, Pet manages Task objects, and Scheduler retrieves the combined task collection through Owner.

### Final Decision

I accepted this architecture because it keeps scheduling logic separated from pet/task storage and allows algorithms to operate across multiple pets.

---

## Scheduler Algorithms

AI helped develop these scheduling features:

### Chronological Sorting

```python
Scheduler.sort_by_time()
```

Sorts tasks by due date and time.

### Filtering

```python
Scheduler.filter_tasks()
```

Filters by pet name or completion status.

### Conflict Detection

```python
Scheduler.detect_conflicts()
```

Detects tasks sharing the same date and time.

### Recurring Tasks

```python
Scheduler.handle_recurring_task()
```

Creates future occurrences for daily and weekly tasks.

### Priority Scheduling

```python
Scheduler.sort_by_priority()
```

Ranks tasks:

```text
high -> medium -> low
```

Tasks with the same priority are sorted by date and time.

### Next Available Slot

```python
Scheduler.next_available_slot()
```

Searches across tasks from all pets and finds the next available interval beginning at or after a requested start time.

---

# Agent Workflow

## Task Requested of the Agent

I asked Agent Mode to implement an advanced scheduling capability:

```text
Add a next_available_slot() method to Scheduler.

Requirements:
- Work across all pets through Owner.get_all_tasks()
- Accept a date, start time, and interval in minutes
- Find the next slot that does not conflict with an existing task
- Add pytest coverage
- Add a CLI demonstration
- Preserve all existing working features
```

## Files Modified by the Agent

The Agent worked on:

```text
pawpal_system.py
main.py
tests/test_pawpal.py
```

## What the Agent Completed

The Agent:

1. Added `Scheduler.next_available_slot()`.
2. Used the Owner's combined task collection so the algorithm works across multiple pets.
3. Added date/time parsing with Python's `datetime`.
4. Advanced candidate times using `timedelta`.
5. Added a CLI demonstration in `main.py`.
6. Added a pytest case where tasks occupied 09:00 and 09:30 and the next 30-minute slot was correctly returned as 10:00.

## Manual Corrections and Human Intervention

The Agent initially attempted to run pytest using a different system Python environment.

That environment did not contain pytest, so the Agent then attempted to install dependencies globally.

I rejected that action because the project already had an existing `.venv`.

Instead, I kept the code changes and manually verified them from the project's activated virtual environment using:

```bash
python -m pytest
python main.py
```

This was an important example of why Agent actions still require human supervision.

I also ensured that the runtime persistence file `data.json` was excluded from Git rather than committed to the repository.

---

## Data Persistence

### Task

Add persistence so pets and tasks remain available between application runs.

### AI Suggestion

Use JSON serialization through the Owner class.

### Implementation

The following methods were added:

```python
Owner.save_to_json()
Owner.load_from_json()
```

Task dates are saved using ISO format and reconstructed using `date.fromisoformat()`.

The Streamlit app automatically loads `data.json` and saves updates.

### Verification

Persistence was verified by:

1. Adding a pet and task.
2. Closing Streamlit.
3. Restarting Streamlit.
4. Confirming the saved data returned.
5. Running the JSON persistence pytest case.

---

## Professional UI Formatting

AI helped improve the Streamlit interface with:

- Dashboard metrics
- Tables
- Emoji indicators
- Priority indicators
- Success messages
- Warning messages
- Error messages
- Care summary metrics

Streamlit functions used include:

```text
st.columns()
st.metric()
st.table()
st.success()
st.warning()
st.error()
```

These changes improve readability without changing the underlying scheduling logic.

---

# Prompt Strategy Comparison

## Strategy 1 — Partial Code Edits

**Model / Tool:** ChatGPT

**Prompt / Task:**  
Provide only the individual method or small code block that needed to change.

### Useful Output

- Short responses
- Easy to study individual algorithms
- Useful when a change is isolated

### Problems

- Partial insertions caused indentation errors.
- Old code sometimes remained in the file.
- One editing sequence resulted in an incorrect self-import.
- It was harder to verify the entire file structure.

---

## Strategy 2 — Complete-File Replacement

**Model / Tool:** ChatGPT

**Prompt / Task:**  
Provide the complete updated file while preserving all existing working functionality.

### Useful Output

- Consistent indentation
- Easier import verification
- Easier class-structure verification
- Lower chance of obsolete code remaining
- Faster copy/run/test workflow

### Problems

- Longer responses
- Full files still require human review
- Manual changes could be overwritten if the replacement is not checked first

---

## Comparison and Final Decision

Both prompting strategies were useful for different purposes.

The incremental strategy was better for understanding isolated concepts.

The complete-file strategy was more reliable for larger structural changes because it reduced integration and indentation errors.

For PawPal+, I ultimately preferred:

```text
small conceptual change -> targeted prompt

multi-method or structural change -> complete-file prompt
```

This comparison directly changed my AI-assisted development workflow.

---

## Accepted, Rejected, and Revised AI Suggestions

### Accepted

I accepted:

- The four-class OOP architecture
- Dataclasses for Task and Pet
- Scheduler access through Owner
- pytest-based verification
- JSON serialization
- Priority-based scheduling
- The next-available-slot algorithm

### Revised

I revised the initial partial-edit workflow after it caused indentation and integration problems.

I switched to complete-file replacements for larger changes.

### Rejected

I rejected the Agent's attempt to install project dependencies globally because the project already had an isolated virtual environment.

I instead used the existing `.venv`.

---

## Testing

The final automated test suite verifies:

1. Task completion
2. Adding tasks to pets
3. Chronological sorting
4. Priority-based sorting
5. Recurring tasks
6. Conflict detection
7. JSON persistence
8. Next available slot scheduling

Final test command:

```bash
python -m pytest
```

Passing result:

```text
8 passed
```

---

## Verification Methods

I used:

```bash
python -m py_compile pawpal_system.py
python main.py
python -m pytest
streamlit run app.py
```

These checks verified:

- Syntax
- OOP behavior
- Scheduling algorithms
- Persistence
- CLI behavior
- Streamlit integration
- Automated tests

---

## Key Takeaway

AI accelerated design, implementation, debugging, and testing, but it did not replace engineering judgment.

The Agent environment issue demonstrated that even when AI-generated code is useful, I still need to evaluate proposed commands, preserve the correct development environment, test the result, and decide which changes should be accepted.