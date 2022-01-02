# ------------------------------------------------------------
# ------------**## Working With Random Values ##**------------

import random

# *-*-*-*-*-*-*-*-*-*-*-*- between zero & one
# print(random.random())

# *-*-*-*-*-*-*-*-*-*-*-*- between two arbitrary numbers
# print(random.randint(1, 50))

# *-*-*-*-*-*-*-*-*-*-*-*- randomly choosing a list item
# print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# *-*-*-*-*-*-*-*-*-*-*-*- randomly choosing multiple list items
# print(random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=2))
# print(random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=5))

# *-*-*-*-*-*-*-*-*-*-*-*- shuffling a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)

print(numbers)
