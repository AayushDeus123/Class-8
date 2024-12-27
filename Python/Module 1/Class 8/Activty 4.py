print('Which of the cyclists speed is slower than the average')
a = int(input("Enter the John's speed : "))
b = int(input("Enter the Jack's speed : ")) 
c = int(input("Enter the Josh's speed : "))

avg = (a+b+c)/3
print('Average of the three cyclists is',avg)

if avg > a and avg > b and avg > c:
    print('All three cyclists are slower than the average speed of',avg)
elif avg > a and avg > b:
    print('John and Jack are slower than the average speed of',avg)
elif avg > a and avg > c:
    print('John and Josh are slower than the average speed of',avg)
elif avg > b and avg > c:
    print('Jack and Josh are slower than the average speed of',avg)
elif avg > a:
    print('John is slower than the average speed of',avg)
elif avg > b:
    print('Jack is slower than the average speed of',avg)
elif avg > c:
    print('Josh is slower than the average speed of',avg)
else:
    print('Invalid input')