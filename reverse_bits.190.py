# Reverse bits of a given 32 bits unsigned integer.

def reverseBits(n):
        a = []
        n = str(n)
        for i in n:           
            a.append(i)
        while len(a) < 32:
            a.insert(0, '0')
        for i in range(16):
            tmp = a[i]
            a[i] = a[len(a) - i - 1]
            a[len(a) - i - 1] = tmp
        st = ''.join(a)
        num = int(st, 2)
        return num

d = 11111111111111111111111111111101

print(d)
print(reverseBits(d))
