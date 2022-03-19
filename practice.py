import modulefinder


num = int(input("Enter a number: "))

mod = num % 2

if mod > 0:
    print("Your number is odd")

else:
    print("Your number is even")