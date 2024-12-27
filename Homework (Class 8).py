#Swapping the values of numbers
a = input("Enter value number A: ")
b = input("Enter value number B: ")
c = input("Enter value number C: ")

a, b, c = c, a, b
print(f"After swapping: A = {a}, B = {b}, C = {c}")