import unittest
from scheduler import TaskScheduler


class TestTaskScheduler(unittest.TestCase):

    def test_basic_case(self):
        #example from the case
        tasks = {
            "A": {"time": 3, "deps": []},
            "B": {"time": 2, "deps": []},
            "C": {"time": 4, "deps": []},
            "D": {"time": 5, "deps": ["A"]},
            "E": {"time": 2, "deps": ["B", "C"]},
            "F": {"time": 3, "deps": ["D", "E"]},
        }

        scheduler = TaskScheduler(tasks)
        order, min_time = scheduler.calculate()

        # minimum time should be 11 based on critical path
        self.assertEqual(min_time, 11)

        # order should include all tasks
        self.assertEqual(len(order), len(tasks))


    def test_cycle_detection(self):
        # this case has a cycle: A -> B -> A
        tasks = {
            "A": {"time": 3, "deps": ["B"]},
            "B": {"time": 2, "deps": ["A"]},
        }

        scheduler = TaskScheduler(tasks)

        with self.assertRaises(ValueError):
            scheduler.calculate()


if __name__ == "__main__":
    unittest.main()