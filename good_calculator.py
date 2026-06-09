# This file follows recommened coding practices.

def add(first_number, second_number):
  """Return the sum of two numbers."""
  return first_number + second_number

def subtract(first_number, second_number):
  """Return the difference between two numbers."""
  return first_number - second_number

def multiply(first_number, second_number):
  """Return the product of two numbers."""
  return first_number * second_number

def divide(first_number, second_number):
  """Return the quotient of two numbers."""
  if second_number == 0:
    return "Error: Cannot divide by zero.")
  return first_number / second_number

def display_menu():
  """Display the calculator options."""
  print("Welcome to the calculator")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")

def get_number(prompt):
    """Ask the user for a number and return it as a float."""
    return float(input(prompt))

def calculate(choice, first_number, second_number):
    """Choose the correct operation based on the user's menu choice."""
    operations = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide,
    }

    operation = operations.get(choice)
    if operation is None:
        return "Invalid choice."

    return operation(first_number, second_number)

def main():
    """Run the calculator program."""
    display_menu()
    choice = input("Enter choice: ")
    first_number = get_number("Enter first number: ")
    second_number = get_number("Enter second number: ")
    result = calculate(choice, first_number, second_number)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
