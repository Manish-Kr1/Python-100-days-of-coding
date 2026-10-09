print ("Mini calculator ")

num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))

print("press 1 for addition \n press 2 for sbtraction \n press 3 for multiplication \n press 4 for division")

choice = int(input("enter your choice  from 1 - 4"))

if choice == 1:
    print("the  addition of given number is ", num1 + num2)

elif choice == 2:
    print("the  subtraction of given number is ", num1 - num2)

elif choice == 3:
    print("the  multiplication of given number is ", num1 * num2)

elif choice == 4:
    print("the  Division of given number is ", num1 / num2)

else:
    print("enter a valid range")