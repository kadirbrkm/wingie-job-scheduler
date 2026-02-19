from collections import defaultdict, deque

class TaskScheduler:
    def __init__(self, tasks):
        # tasks will be given as a dictionary
        # each task has a duration and a list of dependencies
        self.tasks = tasks

        # adjacency list representation of the graph
        self.graph = defaultdict(list)

        # keeps how many dependencies each task has
        self.in_degree = defaultdict(int)

        # will store the earliest completion time of each task
        self.completion_time = {}

    def build_graph(self):
        # now initialize in-degree for each task
        # this will help me track how many dependencies each task has
        for task in self.tasks:
            self.in_degree[task] = 0

        # build the adjacency list
        # if task D depends on A, we create an edge A -> D
        for task, info in self.tasks.items():
            for dependency in info["deps"]:
                self.graph[dependency].append(task)
                self.in_degree[task] += 1  

    def topological_sort(self):
        queue = deque()
        order = []

        # add tasks that have no dependencies
        for task in self.tasks:
            if self.in_degree[task] == 0:
                queue.append(task)
                self.completion_time[task] = self.tasks[task]["time"]

        while queue:
            current = queue.popleft()
            order.append(current)

            for neighbor in self.graph[current]:
                self.in_degree[neighbor] -= 1

                # update earliest completion time
                self.completion_time[neighbor] = max(
                    self.completion_time.get(neighbor, 0),
                    self.completion_time[current] + self.tasks[neighbor]["time"]
                )

                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # if not all tasks are processed, there is a cycle
        if len(order) != len(self.tasks):
            raise ValueError("Cycle detected in task dependencies")

        return order
    
    def calculate(self):
        # first build the graph structure
        self.build_graph()

        # then get the execution order
        order = self.topological_sort()

        # the job finishes when the last task finishes
        # so i take the maximum completion time
        min_time = max(self.completion_time.values())

        return order, min_time