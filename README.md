\# CLI Task Manager



A command-line task management tool built in Python, using a custom-built linked list for data storage instead of Python's built-in list — implemented from scratch to apply core data structures and algorithms concepts.



\## Features



\- Add tasks with a title and priority (High/Medium/Low)

\- View all tasks with their current status

\- Mark tasks as complete

\- Delete tasks

\- Sort tasks by priority (custom bubble sort implementation)

\- Persistent storage — tasks are saved to a file and reloaded automatically



\## Tech Stack



\- Python (no external libraries — built entirely with the standard library)

\- Custom linked list (`TaskNode`, `TaskList`) for task storage

\- File I/O for persistence



\## How to Run



1\. Clone this repository:

2\. Run the program:

3\. Follow the on-screen menu to add, view, complete, delete, or sort tasks.



\## Project Structure

\## Documentation



See the \[Software Requirements Specification](docs/SRS.md) for full project scope and requirements.



\## Design Decisions



\- \*\*Custom linked list over Python's built-in list\*\*: chosen to directly apply data structures concepts, and because insertion/deletion doesn't require shifting elements the way an array-based list does.

\- \*\*Bubble sort for priority sorting\*\*: implemented manually rather than using Python's built-in `sort()`, to demonstrate understanding of sorting algorithms.

\- \*\*Plain text file storage\*\*: kept simple and human-readable for this stage of the project; could be upgraded to SQLite or JSON in a future iteration.



\## Sample Interaction

\## Status



Completed as part of a structured portfolio-building plan — first of three CV projects.



