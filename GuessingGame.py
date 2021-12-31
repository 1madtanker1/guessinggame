#####PYTHON GUESSING GAME
import random

print("Ok I have made up my number, enter 3 numbers")
print("If the sum of your numbers islarger than the number I guessed, you win!")

num1 = int(input("Enter your first number > "))

num2 = int(input("Enter your second number > "))

num3 = int(input("Enter your third number > "))

numbers = [num1, num2, num3]

var1 = int(sum(numbers))
var2 = random.randint(1, 1024)

if var1 > var2:
    print("You won!")

else:
    print("you lost")

print("my number was")
print(var2)
