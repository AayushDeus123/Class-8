#Divisible Number
num = int(input('Enter your Numerator : '))
den = int(input('Enter your Denominator : '))
a = num//den
if num%den==0:
    print(num,'is divisible by',den,'and is equal to',a)
else:
    print('The numbers given are not divisible without a remainder')