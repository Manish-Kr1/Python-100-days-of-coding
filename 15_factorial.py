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

# Solution 2 using recursion 


def fact(a):
    if a==0:
        return 1
    else:
        return((a)*fact(a-1))

num = int(input("Enter a number here: "))

result = fact(num)
print("the factorial of the given number is ", result)
    

