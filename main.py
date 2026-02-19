from scheduler import TaskScheduler


def main():
    # defining the sample tasks based on the case example
    tasks = {
        "A": {"time": 3, "deps": []},
        "B": {"time": 2, "deps": []},
        "C": {"time": 4, "deps": []},
        "D": {"time": 5, "deps": ["A"]},
        "E": {"time": 2, "deps": ["B", "C"]},
        "F": {"time": 3, "deps": ["D", "E"]},
    }
    # create scheduler instance
    scheduler = TaskScheduler(tasks)

    # calculate execution order and minimum completion time
    order, min_time = scheduler.calculate()

    print("Execution Order:", order)
    print("Minimum Completion Time:", min_time)


if __name__ == "__main__":
    main()