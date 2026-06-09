print("Welcome to the BAD calculator")

#Menu text
print("Choose an option:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice: ")
num1 = float(input("Enter first number: ")
num2 = float(input("Enter second number: ")

# Each function does too many things: calculation, printing, and validation.
# Lot of repeated code
def doStuff1(a, b):
    print("The answer is:")
    print(a + b)
    print("Thanks for using the calculator")

def doStuff2(a, b):
    print("The answer is:")
    print(a - b)
    print("Thanks for using the calculator")

def doStuff3(a, b):
    print("The answer is:")
    print(a * b)
    print("Thanks for using the calculator")

def doStuff4(a, b):
    print("The answer is:")
    if b == 0:
        print("Error")
    else:
        print(a / b)
    print("Thanks for using the calculator")

# YAGNI violation: unnecessary functions that are not used by the program.
def scientificSuperAdvancedModeThatDoesNothing():
  print("This future feature is not needed yet")

def calculatorWithInheritanceThatIsNotNeeded():
  print("This program does not need inheritance")

# Long if/elif chain with repeated logic.
if choice == "1":
  doStuff(num1, num2)
elif choice == "2":
  doStuff2(num1, num2)
elif choice == "3":
  doStuff3(num1, num2)
elif choice == "4":
  doStuff4(num1, num2)
else:
  print("Invalid choice")
  print("Thanks for using the calculator")
