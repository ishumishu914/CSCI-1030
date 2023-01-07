import random 

def simulate_game():
    num_in_row = 0 
  
    for i in range (200):
        randNum = random.randint(1, 6)
    
        if randNum != 6: 
            num_in_row += 1
        
            if num_in_row == 20: 
                return True 
        else: 
            num_in_row = 0 
    return False 

success = 0 
for round in range(1000):
    if simulate_game() == True:
        success += 1 

print(f'Probability: {success}/1000 =', success / 1000)