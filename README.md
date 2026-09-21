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


prob12 --> Write a program to print Prime numbers  in range

       lower = int(input("Enter lower limit here "))
       upper = int(input("Enter upper limit here "))
       
       for num in range(lower, upper+1):
           if num > 1:
               for i in range(2, num):
                   if num%i == 0:
                       break
       
               else:
                   print(num)

prob13 --> write a program to convert Celsius into Fahrenheit

      celcius = int(input("enter the tempereture in celcius "))
      
      farenhite  = (celcius*(9/5))+32
      
      print("the converted value is ", farenhite)

prob14 --->write a program  to find the sum of natural numbers after taking input from user

      num = int(input("enter a natural num "))
      
      if num<0:
          print("please enter a positive number")
      
      else:
          sum = 0
          while num > 0:
              sum +=num
              num  -= 1
      
          print(sum)**


prob15 --> Write a program to find factorial of a number

      num = int(input("enter a number "))

      factorial = 1

      if num < 0:
           print("factorial of this number does not exist ")

      if num == 0:
           print("factorial of 0 is ", 1)

     else:
         for i in range(1, num+1):
            factorial = i * factorial

          print("Factorial of ",num ," is ", factorial )


Solution 2 using recursion 

    def fact(a):
    if a==0:
         return 1
    else:
            return((a)*fact(a-1))
    
    num = int(input("Enter a number here: "))
    
    result = fact(num)
    print("the factorial of the given number is ", result)
    


