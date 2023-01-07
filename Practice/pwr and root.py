num = int(input("Enter an integer: "))
pwr = 1
root = 0
found = False
if num < 0:
    neg = True
else:
    neg = False
while pwr < 6:
    while abs(root**pwr) <= abs(num):
        if root**pwr == num:
            print(str(root) + "**" + str(pwr) + " = " + str(num))
            found = True
        if abs(root) > abs(num):
            root = 0
        elif neg:
            root -= 1
        else:
            root +=1
    pwr += 1
    root = 0
if not found:
    print(f"No pair of integers, 'root' and 'pwr', exists such that 0 < pwr < 6 and root**pwr = {num}" )