# Reverse bits of a given 32 bits unsigned integer.

def reverseBits(n):
        for i in range(2, len(str(n))):
            a = []
            for i in str(bin(n)):
                print(i)
                a.append(i)
        for i in range(len(a)):
            if a[i] == '1':
                a[i] = '0'
            else:
                a[i] = '1'
        return ''.join(a)

d = 82
print(d)
print(reverseBits(d))