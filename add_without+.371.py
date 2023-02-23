# Given two integers a and b, return the sum of the two integers 
# without using the operators + and -.

def getSum(a, b):
    while b:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

a = 55
d = 9
print(getSum(a, d))
# բացասական թվերի համար սխալա աշխատում(((