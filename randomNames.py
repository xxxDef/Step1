import random

class MyRandom:
      count : int = 0
      def __init__(self, cnt : int) -> None:
            self.count = cnt

      def random_name(self) -> None:
            #1. Create a list of first names
            first_names: list[str] = ["John", "Mary", "Jack", "Jane", "Emily", "David", "Michael", "Sarah", "Mark", "Elizabeth"]

            #2. Create a list of last names
            last_names: list[str] = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

            #3. Combine them randomly into a list of 100 full names

            for _ in range(self.count):
                  index_first: int = random.randint(0, len(first_names)-1)
                  index_last = random.randint(0, len(last_names)-1)
                  print(first_names[index_first] + " " + last_names[index_last])

            return 1