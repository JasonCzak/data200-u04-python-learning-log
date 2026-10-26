"""Convert a temperature from degrees Celsius to degrees Fahrenheit.

Fictional sample log entry: a model of the expected level of detail,
not real student work.
"""

# Ask the user for a temperature and convert the typed text to a decimal number.
celsius = float(input("Enter temperature in Celsius: "))

# Apply the Celsius-to-Fahrenheit conversion formula.
fahrenheit = (celsius * 9 / 5) + 32

# Display the converted value with two digits after the decimal point.
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")
