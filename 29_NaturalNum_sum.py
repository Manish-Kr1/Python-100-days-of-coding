def NNS (n):
    if n<=1:
       return n
    else:
       return  (n)+NNS(n-1)

n = int(input("enter a number here: "))

if n <= 0:
   print("enter a positive number ")

else:
   print("The sum of natural number uptogiven number is", NNS(n))