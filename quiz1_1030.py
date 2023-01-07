""" # vairable declaration
sentence = str(input('Please enter a sentence: '))
vowel_counts = 0
words = sentence.split(' ')

# process
for v in words:
    if v == 'a' or v == 'e' v == 'i' or v == 'o' or v == 'u': 
    vowel_counts += 1

    # output
    print(f"[{vowel_counts}]")"""

sentence = 'she sells sea shells by the sea shore'
vowel_counts = []
count = 0

for ch in sentence:
    if ch == " ":
        vowel_counts.append(count)
        count=0
    elif ch == 'a' or ch == 'e'or ch == 'i' or ch == 'o' or ch == 'u':
        count+=1

vowel_counts.append(count)
print(vowel_counts)