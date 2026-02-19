# Wingie Enuygun Group - Junior Software Developer Case

## Problem

In this case, I am given a job that consists of multiple tasks.
Each task has a unit completion time and may depend on other tasks.

The objective is to calculate the minimum time required to complete the job and determine a valid execution order of the tasks.


## My Approach

When I analyzed the problem, I realized that it can be modeled as a graph structure.

Each task can be treated as a node, and dependencies between tasks form directed edges.
Since a task cannot be completed before its dependencies, the structure must follow a topological order.

I implemented the solution using an adjacency list representation for the graph and Kahn’s algorithm for topological sorting.
While performing the topological sort, I also calculated the earliest completion time of each task.

To determine the minimum job completion time, I tracked the longest dependency chain (critical path).
Since independent tasks can run in parallel, the total job time is determined by the task that finishes last.

I added cycle detection to ensure invalid dependency graphs are handled properly.
If a cycle exists, the program raises a `ValueError`.

I also added basic unit tests to validate both normal execution and cycle scenarios.

Depending on interpretation, the problem may allow different solutions.
I assumed tasks can run in parallel if they have no dependencies.


## How to Run

Run the main example:

```bash
python main.py
