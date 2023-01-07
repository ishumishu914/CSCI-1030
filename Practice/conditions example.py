'''import math
x = 1.0
sinx = 0.0

for i in range(10):
    term = (-1)**i/math.factorial((2**i)+1)
    sinx += (term*(x**(2*i+1)))
    
print(f'sin(x) approximated is {sinx}')'''

def getWordSize(word):
    if word == '':
        return 0
    else:
        return 1 + getWordSize(word[1:])

print(getWordSize("hello"))
