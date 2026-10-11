# PawPal+ Project Reflection

## 1. System Design

### Core user actions
1. Add and manage pets under an owner.
2. Add care tasks such as feeding, walks, medication, and appointments.
3. View an organized daily schedule across all pets, including conflicts and recurring tasks.

### Initial class design
- **Owner**: Stores owner information and manages multiple pets. It can add pets and retrieve tasks across all pets.
- **Pet**: Stores pet information and manages that pet's tasks.
- **Task**: Represents one care activity with a description, time, frequency, priority, and completion status.
- **Scheduler**: Organizes tasks across all pets. It will sort tasks, filter them, detect scheduling conflicts, and handle recurring tasks.

The relationships are: an Owner has multiple Pets, each Pet has multiple Tasks, and the Scheduler works with the Owner to organize tasks across all pets.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
