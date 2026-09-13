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










      
      print(km, "kms in miles is equal to ", mile, "miles")
