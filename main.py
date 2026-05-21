print("=" * 50)
print("         DODO CHATBOT ASSIGNMENT")
print("=" * 50)

# --------------------------------
# TASK 1 : TALK TO ME
# --------------------------------
print("\nTASK 1 : TALK TO ME")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"\nHello {name}!")
print(f"You are {age} years old.")

# --------------------------------
# TASK 2 : REPEAT YOURSELF
# --------------------------------
print("\n" + "=" * 50)

print("TASK 2 : REPEAT ANYTHING")

repeat_name = input("Enter a anything: ")
number = int(input("How many times to repeat? "))

print("\nOutput:\n")

for i in range(number):
    print(f"{i + 1}. {repeat_name}")

# --------------------------------
# TASK 3 : ADD NUMBERS FUNCTION
# --------------------------------
print("\n" + "=" * 50)
print("TASK 3 : ADD NUMBERS FUNCTION")


def add_numbers(a, b):
    total = a + b

    print(f"\nAdded Number = {total}")

    if total % 2 == 0:
        print("The number is EVEN")
    else:
        print("The number is ODD")


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

add_numbers(x, y)

# --------------------------------
# FINAL MESSAGE
# --------------------------------
print("\n" + "=" * 50)
print("ALL TASKS COMPLETED SUCCESSFULLY")
print("Thank you for using DODO Chatbot")
print("=" * 50)