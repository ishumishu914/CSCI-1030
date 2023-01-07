values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
is_power_of_2 = []

for num in values:
  if num>1:
    for i in range(2,num):
      n=2**i
      if num%n==0:
        is_power_of_2.append(False)
        break
    else:
      is_power_of_2.append(True)

print(is_power_of_2)

# asnwer
for i in range(len(values)):
  if values[i] == 1 or values[i] == 2:
    is_power_of_2.append(True)
  else:
    while values[i] > 2:
      values[i] == values[i]/2      
      if values[i] == 2:
        is_power_of_2.append(True)

    if values[i] < 2:
      is_power_of_2.append(False)
      
print(is_power_of_2)
