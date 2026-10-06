def findHCF(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf  

x = 12
y = 30

print ("HCF of the given numbers is", findHCF(x, y))