# Write a function that takes the binary representation of 
# an unsigned integer and returns the number of '1' bits it 
# has (also known as the Hamming weight).

def count_1_bit(n):
    a = bin(n)
    return a.count('1')

print(count_1_bit(5))