\# SRS: CLI Task Manager



\## 1. Purpose

A command-line tool to add, view, update, delete, and prioritize personal tasks,

with data saved between sessions.



\## 2. Scope

\- In scope: task CRUD, priority sorting, persistence to file

\- Out of scope: GUI, multi-user support, cloud sync



\## 3. Functional Requirements

\- FR1: User can add a task with a title and priority (High/Medium/Low)

\- FR2: User can view all tasks, sorted by priority

\- FR3: User can mark a task as complete

\- FR4: User can delete a task

\- FR5: Tasks persist after the program closes (saved to a file)



\## 4. Non-Functional Requirements

\- Should run on Windows via terminal

\- Should handle invalid input without crashing (e.g., empty title)



\## 5. Data Structure Plan

\- Tasks stored in a custom linked list (not Python's built-in list)

\- Each node: {id, title, priority, completed}



\## 6. Sample Interaction

> add "Finish CV" high

> list

1\. \[High] Finish CV - Pending

> complete 1

> list

1\. \[High] Finish CV - Done

