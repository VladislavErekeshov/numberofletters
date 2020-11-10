# a = aaabbbbcc
# b = a3b4c2

a = "aaabbbbccdddddeeeggggggggggggggggggrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrllllllllllllllllllllllllllllllllllllllllbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
b = ""
n = 0
m = 0


for i in range(0, len(a)):
    if i == len(a) - 1:
        m += 1
        b += str(a[n])
        b += str(m)

    else:
        if a[i] == a[n]:
            m += 1
        else:    
            b += str(a[n])
            b += str(m)
            m = 1
            n = a.index(a[i])



print(b)
