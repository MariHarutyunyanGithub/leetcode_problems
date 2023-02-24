# Given two integers a and b, return the sum of the two integers 
# without using the operators + and -.

def getSum(a, b):
    mask = 0xffffffff
    while b:
        carry = (a & b) 
        a = (a ^ b) & mask
        b = (carry << 1)& mask
    if (a >> 31) & 1:
        return a | ~(mask)
    return a

a = -5
d = 9
print(getSum(a, d))
