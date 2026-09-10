# Python-100-days-of-coding
# Python-100-days-of-coding

# prob1--> add 2 numbers (taking input from user)

      num1 = float(input("enter num1 "))
      num2 = float(input("enter numm2 "))
      
      print ("sum of two numbers is", num1+num2)

      
# Prob2 --> write a program to find he square root of a number


       num = 64
       num1 = int(input("Enter a number "))
       sr = num1**(1/2) 
      
       print("Square root of the number is ", sr)
      
   Solution 2 using Math module
      
      import math
      num1 = int(input("enter a number "))
      
      sr = math.sqrt(num1)
      
      print("Square root of the number is ", sr)

# prob3 --> Write a program to Fund the area of a triangle

      
      Base = float(input("Enter base of triangle "))
      Height = float(input("Enter height of triangle "))
      
      Area = (Base*Height)/2
      print("area of triangle is ", Area)
