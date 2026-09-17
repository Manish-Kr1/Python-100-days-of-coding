# Python-100-days-of-coding
# Python-100-days-of-coding

 prob1--> add 2 numbers (taking input from user)

      num1 = float(input("enter num1 "))
      num2 = float(input("enter numm2 "))
      
      print ("sum of two numbers is", num1+num2)

      
 Prob2 --> write a program to find he square root of a number


       num = 64
       num1 = int(input("Enter a number "))
       sr = num1**(1/2) 
      
       print("Square root of the number is ", sr)
      
   Solution 2 using Math module
      
      import math
      num1 = int(input("enter a number "))
      
      sr = math.sqrt(num1)
      
      print("Square root of the number is ", sr)

 prob3 --> Write a program to Find the area of a triangle

      
      Base = float(input("Enter base of triangle "))
      Height = float(input("Enter height of triangle "))
      
      Area = (Base*Height)/2
      print("area of triangle is ", Area)

 prob4 ---> write a program to convert Kilo meters into miles


       km = float(input("enter your value in kms "))
      
       mile = (0.621371)*km

       print(km, "kms in miles is equal to ", mile, "miles")


prob5 ---> Write a program to swap two variables

     x = 13
     y = 12
     
     temp = x
     print("the value of temp is ", temp)
     
     x = y
     print("the value of x is ", x)
     
     y = temp
     print("the value of y is ", y)
     
     
     solution 2 without using 3rd variable
     
     x = 12
     y = 13
     
     x, y = y, x
     
     print("the value of x is ", x)
     print("the value of y is ", y)

prob6 --> Program to check if a number is positive negative or Zero

     num = int(input("Enter a number "))
     
     if num > 0:
         print("number is positive ")
     
     elif num < 0:
         print("number is negative ")
     
     else:
         print("number is 0 ")
 
 prob7 --> Program to  find odd even numbers
      
      num = int(input("Enter a  number "))
       
      if num % 2 == 0 :
          print("number is even")
       
      else:
          print("number is odd")

   prob8 --> Program to find if a year is leap year or not

      year = int(input("enter a year "))
      
      if (year % 100 == 0) & (year % 400 == 0):
          print(year, "is leap year ")
      
      elif (year % 4 == 0) and (year % 100 != 0):
          print(year, "is a leap year ")
      
      else:
          print(year, "is not a leap year ")

       **Output --> enter a year 1996
                  1996 is a leap year**

 prob9 --> write a program to find largest among three numbers

       num1 = float(input("Enter first number: "))
       num2 = float(input("Enter second number: "))
       num3 = float(input("Enter third number: "))
       
       if (num1 >= num2) and (num1 >= num3):
          largest = num1
       elif (num2 >= num1) and (num2 >= num3):
          largest = num2
       else:
          largest = num3
       
       print("The largest number is", largest)


prob10 --> write a program to check if a number is prime number or not

      num = int(input("Enter a number "))
     
      if num <= 1:
          print("it is not a prime number")
      
      if num > 1:
          for i in range (2, num):
              if num % i == 0:
                  print(num, " is not a prime number")
                  break
          else:
              print(num, " is a prime number")

prob11 --> Write a program to print random numbers

       import random   
       
       num = random.randint(0,10)
       
       print (num)

