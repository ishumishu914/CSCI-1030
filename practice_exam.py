""" Q1: Write a Python function, getWordSize(), that takes a single string as argument (word).  
The function must use recursion to determine the length of the string, which is the return value for this function."""

def getWordSize(word):
    if word == '':
        return 0
    else:
        return 1 + getWordSize(word[1:])


def processSentence(sentence, processWord):
    result = []
    array = sentence.split()
    
    for i in array:
        result.append(processWord(i))
    return result
    
print(processSentence('hello my name is lia', getWordSize)) 

""" Using the following function, multiplyMatrices(), as a starting point, use operation
counting (like you did in lab 08) to determine how many numbers get multiplied (in terms of n), 
when calling multiplyMatrices(a, b), where a and b are both lists (of lists) of the same size 
(a and b will have n lists, each list having n elements). 
The += statement is the only operation that you need to count.  Try various values for n (choose carefully!), 
and record the results in a comment inside the file.  Provide your best guess for an expression describing the performance of 
this algorithm (insertionSort was n2, binarySearch was log2n, for example), also in the comments for this function.  """

def multiplyMatrices(a, b):
    n = len(a)
    count = 0

    result = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append(0)
        result.append(row)

    for r in range(n):
        for c in range(n):
            value = 0.0
            for i in range(n):
               value += a[r][i] * b[i][c]   # count only this line
               count+=1
            result[r][c] = value
    return count, result 

x = [[1,2,5], 
     [6,7,10],
     [6,7,10]]
    
y = [[2,3,5], 
     [5,0,2],
     [6,7,10]]

print(multiplyMatrices(x, y)) 
# expression describing the performance of this algorithm: n**3 

'''def processGame(filename, handler):
    with open('game.txt', 'r') as file:
        for line in file:
            content = line
            handler(content)    


def printGame(gameState):
    for i in range(0, len(gameState)):
        print(gameState[i], end=' ')

print(processGame("1 2 3 4 5 6 7 8 9", printGame)) '''

def has_no_repeated_letter(string):
    if len(string) == 1:
        return False
    else:
        for i in range(len(string)):
            for j in range(len(string)):
                if i!=j and string[i]==string[j]:
                    return False
        return True

print('ablewasiereisawelba:', has_no_repeated_letter('ablewasiereisawelba'))
print('abcd:', has_no_repeated_letter('abcd'))

def get_longest_matching_substring(string):
    if len(string) == 0:
        return None
    
    start = maxLength = 0
    used = []
    
    for i in range(len(string)):
        if string[i] in used and start <= used[string[i]]:
            start = used[string[i]] +1
        else:
            maxLength = max(maxLength, i-start+1)
        used[string[i]] =i
    
    return maxLength
    
print('longest with no repeated letter:', get_longest_matching_substring('i saw abba, but ablewasiereisawelba by the racecar'))

import re 
def match_string(string):
    regex = "^[A]{3,5}[B]?[C]*[D|E+]$"
    
    if re.match(regex, string):
        return True
    else:
        return False
        
print(match_string("AAABCCCD"))
print(match_string("AAAAEEEE"))
print(match_string("AAAAABD"))
print(match_string("AAACCCE"))

import re 
def match_address(string):
    regex2 = "^[0-9]*\s[A-Z]{1}[a-z]+\s"
    
    if re.search(regex2, string):
        return True
    else:
        return False
        
print(match_address("2000 Simcoe Road North"))
print(match_address("290 Bremner Blvd"))
print(match_address("123 Apple "))
