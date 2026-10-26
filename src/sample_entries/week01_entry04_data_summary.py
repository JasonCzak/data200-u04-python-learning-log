"""Calculate basic summary statistics for a small example dataset.

Fictional sample log entry: a model of the expected level of detail,
not real student work.
"""

# Store the observations in a Python list.
data = [12, 18, 25, 30, 22, 16, 19]

# Calculate the mean by dividing the sum by the number of observations.
average = sum(data) / len(data)

# Display the original values and three basic summary statistics.
print("Data:", data)
print("Minimum:", min(data))
print("Maximum:", max(data))
print(f"Average: {average:.2f}")
