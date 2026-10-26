"""Classify a numeric score using a standard letter-grade scale.

Fictional sample log entry: a model of the expected level of detail,
not real student work.
"""

# Ask the user for a score and convert the response to a decimal number.
score = float(input("Enter your score: "))

# Select the letter grade. Checking from highest to lowest prevents overlap.
if score >= 90:
    letter_grade = "A"
elif score >= 80:
    letter_grade = "B"
elif score >= 70:
    letter_grade = "C"
elif score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"Grade: {letter_grade}")
