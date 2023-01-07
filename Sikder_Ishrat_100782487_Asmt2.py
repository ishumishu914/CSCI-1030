# Full name: Ishrat Zaman Sikder
# Student ID: 100782487
# Assignment 2
""" Completed in team of 2
    Members: Ishrat Sikder - Student ID: 100782487
             Jessica Patel - Student ID: 100785837 """

""" Part 1: Write a class (Stack) that implements all of the stack operations described in the lectures. """

print("Part 1:\n")

class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty(self): 
        return self.stack == [] 
    
    def push(self,item): 
        self.stack.append(item) 
    
    def pop(self): 
        return self.stack.pop()

    def top(self): 
        if len(self.stack) >= 1:
            return self.stack[len(self.stack) -1]
    
    def __str__(self):
        if self.is_empty():
            return True
        #if self.push():
            #return self.stack

stack = Stack()

print('is_empty():', stack.is_empty())
print('empty:', stack)
stack.push(1)
print('after push(1):', stack)
print('is_empty():', stack.is_empty())
stack.push(10)
print('after push(10):', stack)
print('pop():', stack.pop())
print('after pop():', stack)
stack.push(2)
print('after push(2):', stack)
stack.push(3)
print('after push(3):', stack)
stack.push(4)
print('after push(4):', stack)
print('pop():', stack.pop())
print('after pop():', stack)
print('pop():', stack.pop())
print('after pop():', stack)
print('pop():', stack.pop())
print('after pop():', stack)
print('pop():', stack.pop())
print('after pop():', stack)
print('is_empty():', stack.is_empty())


""" Part 2: Write a function (is_palindrome) that uses a stack to check if a string is a 
    palindrome. The function takes just one argument, the string to check. The function 
    returns True if the string is a palindrome, False otherwise. """

print("Part 2:\n")
    
def is_Palindrome(string):
    length = len(string)
    mid = int(length/2) # find mid character of word
    stack = []
    
    for i in range(0, mid):
        stack.append(string[i]) # push each character in word to stack
        
    if (length % 2) != 0:
        mid += 1 # if word length is odd skip middle character 
    
    while mid < length:
        if stack.pop() != string[mid]: # pop off each character from stack and compare with next character in the string
            return False
        mid += 1 # increment mid to compare next character
    return True 

print(is_Palindrome("level"))
print(is_Palindrome("lever"))
print(is_Palindrome("definitelynotapalindrome"))
print(is_Palindrome("ablewasiereisawelba"))
print(is_Palindrome("ablewasiereisawelbar"))


""" Part 3: Write a function (calculate_rpn) that uses a stack to calculate the result of an 
    expression in Reverse Polish Notation (RPN) (also called Postfix notation) """

print("Part 3:\n")

def is_integer(str):   
    for chr in str:      
        if (chr < '0') or (chr > '9'):         
            return False   
    return True

def to_integer(str):   
    return int(str)

def calculate_rpn(rpnString):
    stack = []

    for token in rpnString.split(' '):
        if(is_integer(token)):
            stack.append(to_integer(token))
        else:
            num1 = stack.pop()
            num2 = stack.pop()

            if (token == '+'):
                stack.append(num2+num1)
            elif (token == '-'):
                stack.append(num2-num1)
            elif (token == '*'):
                stack.append(num2*num1)            
            elif (token == '/'):
                stack.append(num2/num1)   

    return stack.pop()

print(calculate_rpn('7 2 /'))
print(calculate_rpn(' 8 4 * 7 2 / + 4 1 -'))
