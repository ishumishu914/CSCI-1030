# Full name: Ishrat Zaman Sikder
# Student ID: 100782487
# Assignment 1
""" Completed in team of 2
    Members: Ishrat Sikder - Student ID: 100782487
             Jessica Patel - Student ID: 100785837 """

""" Part 1: Write a function (intersect) that takes two lists as input (you can assume they 
have no duplicate elements), and returns the intersection of those two sets (as a list) without 
using the in operator or any built-in functions, except for range() and len(). """

print('PART 1:')
# function to check if any values are present in the two lists
def intersection(s1,s2): 
  list1=[] 

  # loop through both lists
  for i in range(len(s1)): 
    for j in range(len(s2)):
      if s1[i] == s2[j]: # look for matching values in any indices of either lists
        list1.append(s1[i])
  
  # case when no matching values are found
  if len(list1) == 0: 
    print('No intersecting values found')
  return list1

print(intersection([1,3,5,7,9,11,13,15,17,19,21,23,25], [1,4,9,16,25]))


""" Part 2: Write a function (gregory_liebniz) that will estimate π using the Gregory-Liebniz series """

print('PART 2:')
# function to calculate π value using Gregory-Liebniz series
def gregory_liebniz(num_iterations):
  result = 0.0
  
  # loop for iterating through range of term of iteration given
  for i in range(num_iterations):
    result += (-1.0)**i/(2.0*i+1.0) # convergent sum of each result  
  return '%.6f'%(result*4)

print(gregory_liebniz(1000000)) 


""" PART 3: Advanced version of RPG game"""

class Character:
  def __init__(self, name, hp, xp_gained, attack, defense, magic = 0, xp = 0, level = 1):
    self.name = name
    self.hp = hp
    self.max_hp = hp
    self.xp_gained = xp_gained
    self.attack_power = attack
    self.defense_power = defense
    self.magic = magic
    self.xp = xp
    self.level = level

  # function to check if any player/enemy is dead
  def is_dead(self):
    if self.hp <= 0:
      return True
    return False

  # function to print character status (dead/stats)
  def __str__(self):
    if self.is_dead():
      return (self.name, '[DEAD]')
        
    else:
      return  self.name + ' (HP: ' + str(self.hp) + ', XP: ' + str(self.xp) + ', Level: ' + str(self.level) + ', Attack: ' + str(self.attack_power) + ', Defense: ' + str(self.defense_power) + ')'

  # function to attack players 
  def attack(self, other_character):

    # checks if the player is dead except Glinda
    if self.is_dead():
      if self.name != 'Glinda':
        print(self.name, ' cannot attack because s/he is dead.')

    # if player is Glinda proceed to heal function 
    elif self.name == 'Glinda':
      self.heal(party)

    # if the player isn't Glinda then calculate attack & damage of characters 
    else:
      # check if the attack_power > defense power; if so then attack 
      if other_character.defense_power <= self.attack_power:
        # damage done to the other player
        damage = self.attack_power - other_character.defense_power

        #calculate remaining hp
        other_character.hp -= damage
        print(self.name, 'does', damage, 'points of damage to', other_character.name)

      # print zero damage done when the above condition is false
      else:
        print(self.name, 'does 0 points of damage to', other_character.name)

      # prevents hp from going below 0
      if other_character.hp <= 0:
        other_character.hp = 0
        print(other_character.name, 'has been defeated.')

        # attack function called gain function to increase xp and level of the character
        self.gain_xp(other_character)

  #function for Glinda to heal party 
  def heal(self, party):
    # check if Glinda is dead 
    if self.is_dead():
      if self.name == 'Glinda':
        print(self.name, 'cannot heal because s/he is dead.')

    else:
      for party_member in party:
        #if the the party member is not dead and hp < max_hp Glinda heals 
        if not party_member.is_dead() and party_member.hp < party_member.max_hp:
          party_member.hp += self.magic

          # prevent hp of current party member from exceeding max_hp
          if party_member.hp > party_member.max_hp:  
            party_member.hp = party_member.max_hp

          print(self.name, 'heals', self.magic, 'hp for', party_member.name)

        # print zero damage done when the above condition is false
        else:
          print(self.name,'heals 0 hp for',party_member.name)

  # function used to gain points/level-up for a player 
  def gain_xp(self, other_character):
    levelUp = True

    if not self.is_dead() and other_character.is_dead(): 
      #current player gains points 
      self.xp += other_character.xp_gained
      print(self.name, 'gained', other_character.xp_gained, 'XP')
      
      # level up players
      while levelUp and self.level < levels[len(levels) - 1]:
        # self.level used as an index to access level related attributes
        if self.xp >= level_min_xp[self.level - 1]:
          self.attack_power += level_attack_gain[self.level - 1]
          self.defense_power += level_defense_gain[self.level - 1]
          self.magic += level_magic_gain[self.level - 1]
          self.level = levels[self.level - 1]
          print(f'{self.name} leveled up to level {self.level}')
          levelUp = True
        else:
          levelUp = False

# additional game information
krogg = Character('Krogg', 180, 0, 20, 20)
glinda = Character('Glinda', 120, 0, 5, 20, 5)
geoffrey = Character('Geoffrey', 150, 0, 15, 15)
party = [krogg, glinda, geoffrey]
enemy1 = Character('Spider 1', 50, 100, 10, 1)
enemy2 = Character('Spider 2', 50, 100, 10, 1)
enemy3 = Character('Wolf 1', 100, 250, 15, 5)
enemy4 = Character('Wolf 2', 100, 250, 15, 5)
enemy5 = Character('Bear 1', 200, 350, 20, 10)
enemy6 = Character('Bear 2', 200, 350, 20, 10)
enemy7 = Character('Red Dragon', 300, 800, 30, 20)
enemy8 = Character('Blue Dragon', 400, 1000, 35, 20)
enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7,enemy8]
totaEnemies = 8

levels = [2, 3, 4, 5, 6]
level_min_xp = [100, 200, 300, 400, 500]
level_attack_gain = [5.0, 2.5, 2.5, 2.5, 2.5]
level_defense_gain = [2.5, 2.5, 2.5, 2.5, 2.5]
level_magic_gain = [2.0, 1.0, 2.0, 2.0, 2.0]

print('PART 3:')

# game runs as long as valid
isValid = True
while (isValid == True):

  party_index = [0, 1, 2] #index of pary members in party to run code
  roundNum = 1 # battle begins from round 1
  enemy_count = 0 # count number of dead enemies

  #function for checking if all enemies are dead
  def enemyDeadCheck():
    deadCheck = False
    for enemy in enemies:
      if enemy.is_dead():
        deadCheck = True
      else:
        deadCheck = False
    return deadCheck

  # main battle-loop
  while enemy_count < totaEnemies:

    print("\nRound", roundNum,'\n')
    print("Action:")

    for i in party_index:
      party[i].attack(enemies[enemy_count])

      if enemies[enemy_count].is_dead():
        enemy_count += 1  # move on to the next enemy once current one is defeated
        if enemy_count == totaEnemies:  # break out of loop once gone out of range
          break

    # check if the party has won the battle
    if enemyDeadCheck():
      print('The enemies are dead. You are victorious!')
      isValid = False
      break

    # enemies attack the party members 
    for i in range(len(party)):
      enemies[enemy_count].attack(party[i])

    # prints character status and final result (players & enemies)
    print('\nCharacter Status:')
    for partyMember in party:
      print(partyMember.__str__())
    for enemy in enemies:
      print(enemy.__str__())

    # not taking party losing case into account as we have knowledge of output already
      
    roundNum += 1 # increment round