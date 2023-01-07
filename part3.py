class Character:     
  def __init__(self, name, hp, xp_gained, attack, defense, level = 1, magic = 0, xp = 0):
    self.name = name         
    self.hp = hp         
    self.max_hp = hp         
    self.attack_power = attack         
    self.defense_power = defense         
    self.magic = magic     
    self.xp_gained = xp_gained
    self.xp = xp
    self.level = level
  
  def __str__(self):
    return '\nCharacter status: \n' + self.name + ' (HP:' + str(self.hp) + ', XP:' + str(self.xp) + ', Level:' + str(self.level) + ', Attack:' + str(self.attack_power) + ', Defense:' + str(self.defense_power) + ', Magic:' + str(self.magic) + ')\n'
  
  def is_dead(self):         
    if self.hp <= 0:             
      return True         
    return False     

  def gain_xp(self, xp):
    self.xp = self.xp + xp

    totalLvls = 5  # 6 levels but for loop starts from 0
    for i in range(totalLvls):
      if self.xp >= level_min_xp[i]:
        self.level = levels[i]
        self.attack_power += level_attack_gain[i]
        self.defense_power += level_defense_gain[i]
        self.magic += level_magic_gain[i]
   
  def attack(self, other_character):         
    if self.is_dead():             
      print(self.name, 'cannot attack because s/he is dead.')

    else:             
      damage = self.attack_power - other_character.defense_power             
      other_character.hp -= damage    

      if other_character.hp <= 0:                 
        other_character.hp = 0  
      if (damage < 0):
        dmg = 0
      else: 
        dmg = damage  

      print(self.name, 'does ', dmg , ' points of damage to', other_character.name)  

      if other_character.is_dead():
        print(other_character.name, ' has been defeated.')
        self.gain_xp(other_character.xp_gained)  
  
  def heal(self, party):         
    if self.is_dead():             
      print(self.name, 'cannot heal because s/he is dead.')     

    else:             
      for party_member in party:                 
        if not party_member.is_dead():                     
          party_member.hp += self.magic       

          if party_member.hp > party_member.max_hp:                         
            party_member.hp = party_member.max_hp 

        print(self.name, ' heals ', self.magic, ' hp for ', party_member.name)
  
levels = [2,3,4,5,6] 
level_min_xp = [100,200,300,400,500]
level_attack_gain = [5.0,2.5,2.5,2.5,2.5] 
level_defense_gain = [2.5,2.5,2.5,2.5,2.5] 
level_magic_gain = [2.0,1.0,2.0,2.0,2.0]
  
krogg = Character('Krogg', 180, 0, 20, 20) 
glinda = Character('Glinda', 120, 0, 5, 20, magic = 5) 
geoffrey = Character('Geoffrey', 150, 0, 15, 15) 
party = [krogg, glinda, geoffrey] 
enemy1 = Character('Spider 1', 50,100, 10, 1) 
enemy2 = Character('Spider 2', 50,100, 10, 1) 
enemy3 = Character('Wolf 1', 100,250, 15, 5) 
enemy4 = Character('Wolf 2', 100,250, 15, 5) 
enemy5 = Character('Bear 1', 200,350, 20, 10) 
enemy6 = Character('Bear 2', 200,350, 20, 10) 
enemy7 = Character('Red Dragon', 300,800, 30, 20) 
enemy8 = Character('Blue Dragon', 400,1000, 35, 20) 
enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8]  

roundNum = 1
totalPartyMem = 3
totalEnemy = 8
currentEnemy = 0  # first enemy index to start
allPmDd = False # all party member dead
allEnDd = False # all enemy dead

while(True):
  print(f'\nRound: {roundNum}\n')

  # each party member attacks
  for partyMem in range(totalPartyMem):

    while party[partyMem].is_dead(): # get the next live party member 
      partyMem = partyMem + 1

      if (partyMem == totalPartyMem): # no nore living party member
        allPmDd = True
        break

    if not allPmDd:
      # check if all enemies are not alreday dead
      enemyDeadCount = 0

      for enemy in enemies:
        if enemy.is_dead():
          enemyDeadCount = enemyDeadCount + 1
      if enemyDeadCount == totalEnemy:
        allEnDd = True
        break   

      # if we reach here there is/are alive enemies
      while enemies[currentEnemy].is_dead(): # get the index of next live enemy
        currentEnemy = currentEnemy + 1
        if (currentEnemy == totalEnemy): #start from first index
          currentEnemy = 0
          
    party[partyMem].attack(enemies[currentEnemy])

    # Heal
    for partyMember in party:
      if partyMember.magic > 0: 
        party[1].heal(party)   

 # current enemy attacks
  for partyMem in range(totalPartyMem):

    while party[partyMem].is_dead(): # get the next live party member's index
      partyMem = partyMem + 1
      if partyMem == totalPartyMem: #no nore living party member
        allPmDd = True
        break

    if not allPmDd:
      # check if all enemies are not already dead
      enemyDeadCount = 0

      for enemy in enemies:
        if enemy.is_dead():
          enemyDeadCount = enemyDeadCount + 1

      if enemyDeadCount == totalEnemy:
        allEnDd = True
        break    

      # if we reach here there is/are alive enemies
      while enemies[currentEnemy].is_dead(): # get the index of next live enemy
        currentEnemy = currentEnemy + 1

        if currentEnemy == totalEnemy:  #start from first ind
          currentEnemy = 0
      enemies[currentEnemy].attack(party[partyMem])
 
  # print character status
  for partyMembers in party:
    if partyMembers.is_dead():
      print (partyMembers.name, ' [DEAD]')
    else: 
      partyMembers.__str__()

  for enemy in enemies:
    if enemy.is_dead():
      print(enemy.name, ' [DEAD]')
    else:
      enemy.__str__() 
 
  # Now see if the game should stop or not 
  # check if all enemies are dead
  deadEnemy = 0
  for enemy in enemies:
    if enemy.is_dead():
      deadEnemy = deadEnemy + 1

  # check if all from party are dead
  deadPm = 0
  for partyMembers in party:
    if partyMembers.is_dead():
      partyMembers = deadPm + 1

  # if all enemies are dead but not all from party, party wins 
  if (deadEnemy == totalEnemy and deadPm < totalPartyMem):
    print('All Enemies are Dead !!! You are Victorious !!!')    
    break

  # if all enemies are not dead but all from party are, enemy wins 
  elif (deadEnemy < totalEnemy and deadPm == totalPartyMem):
    print('All members of Party are Dead !!! You Lost !!!')    
    break

  # if all from both team dies, it's a tie 
  elif  (deadPm == totalPartyMem and deadEnemy == totalEnemy):
    print('All are dead ....')
    break
    
  roundNum += 1 