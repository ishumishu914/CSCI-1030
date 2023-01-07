def reverse_odds(numbers):
    odd_numbers = []
    
    for i in range(len(numbers)):
        if (numbers[i]%2) != 0:
            odd_numbers.insert(0,numbers[i])
            
    reverse_odd_numbers = []
    for j in odd_numbers:
        reverse_odd_numbers.append(j)
    return reverse_odd_numbers 

numbers1 = [1,2,3,4,5,6,7,8,9,10,11,12]
print(f'reverse_odds({numbers1}) =>', reverse_odds(numbers1))

numbers2 = [6,15,-1,8,10,3,-7,9,11,-12]
print(f'reverse_odds({numbers2}) =>', reverse_odds(numbers2))