"""Collect five numbers and calculate their arithmetic mean.

Fictional sample log entry: a model of the expected level of detail,
not real student work.
"""

# The running total must be created before the loop so it is not reset.
total = 0.0
number_of_values = 5

for entry_number in range(1, number_of_values + 1):
    number = float(input(f"Enter number {entry_number}: "))
    total += number

average = total / number_of_values
print(f"Average = {average:.2f}")
