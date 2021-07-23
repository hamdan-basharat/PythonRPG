'''
Hamdan Basharat
4000124515
basham1
IBEHS 1P10
Game Bonus Assignment
March 23rd, 2018
Role-playing game that simulates a character hunting monsters. Involves a hub for them to access inventory, go hunt monsters, buy weapons, and exit the game.
'''

# import the required libraries
import random
import sys

# list that is referenced in the store with weapon names and price
weapons = {"Axe":30,"Crossbow":45,"Greatsword":60}

class Player: # creates the the player class
    def __init__(self, name):
        # initial player stats
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.gold = 30
        self.weap = ["Long Sword"] # sets players initial weapon to Long Sword 9not available in list of buyable weapons
        self.currentweap = ["Long Sword"]
        
    @property # shortcut to creating a property that cant be edited
    def attack(self):
        attack = self.base_attack
        if self.currentweap == "Long Sword": # logic statements set an attack value to each of the different weapons
            attack += 5
        
        if self.currentweap == "Axe":
            attack += 15

        if self.currentweap == "Crossbow":
            attack += 20

        if self.currentweap == "Greatsword":
            attack += 40
            
        return attack # returns the attack value property to the current weapon
        

class Ogre: # creates the first enemy class
    def __init__(self, name):
        # initial enemy stats
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 5
        self.goldgain = 10 # amount of gold the enemy drops when it is killed
ogre = Ogre("Ogre") # makes an instance of the enemy class

class Giant: # creates the second enemy class
    def __init__(self, name):
        # intial enemy stats
        self.name = name
        self.maxhealth = 70
        self.health = self.maxhealth
        self.attack = 7
        self.goldgain = 15 # amount of gold the enemy drops when it is killed
giant = Giant("Giant") # makes an instance of the enemy class

def main(): # main function that is called when the code intially runs
    print ("In the world there are those that hunt...") # intro text 
    intro1 = input(" ")
    print ("and those that are hunted.")
    intro2 = input(" ")
    print ("1. Start") # main menu
    print ("2. Exit")
    option = input("-> ")
    if option == "1": # logic statements that either start the game or ends the code
        start()
    elif option == "2":
        sys.exit()
    else:
        main()

def start(): # function that introdues the game 
    print ("You stumble upon a lonely tavern")
    start1 = input(" ")
    print ("'Welcome traveller, we've been seeking a new hunter'")
    start2 = input(" ")
    print ("Are you up for the challenge?")
    start3 = input(" ")
    print ("What is your name hunter?")
    option = input("--> ")
    global player
    player = Player(option) # makes an instance of the player class
    tavern() # calls the tavern function

def tavern(): # unction that serves as the main menu screen within the game
    # displays all the player stats to the user
    print ("\nName: %s" % player.name)
    print ("Attack: %i" % player.attack)
    print ("Gold: %d" % player.gold)
    print ("Current Weapons: %s" % player.currentweap)
    print ("Health: %i/%i\n" % (player.health, player.maxhealth))
    # displays the users game options
    print ("1. Hunt")
    print ("2. Store")
    print ("3. Inventory")
    print ("4. Exit")
    option = input("--> ")
    if option == "1":  # logic statements that calls a function based of the users choice in the tavern menu
        prefight()
    elif option == "2":
        store()
    elif option == "3":
        inventory()
    elif option == "4":
        sys.exit()
    else:
        tavern() # if the user enters a value thats not an option it calls the tavern menu again until they do

def inventory(): # inventory function where the user can call the equip function or go back to the tavern
    print ("1. Equip Weapon")
    print ("2. Back")
    option = input(">>> ")
    if option == "1":
        equip()
    elif option == "2":
        tavern()

def equip(): # equip function where the user can equip a weapon from their inventory
    print ("What do you want to equip?")
    for weapon in player.weap:
        print (weapon) # shows the weapons the user has a available to equip
    print ("2. Back")
    option = input(">>> ")
    if option == player.currentweap: # tells the user that theyve selected to equip a weapon they already have equipped
        print ("You already have that weapon equipped")
        option = input(" ")
        equip()
    elif option == "2": # exits back to the inventory method 
        inventory()
    elif option in player.weap: # equips the weapon the user chose
        player.currentweap = option
        print ("You have equipped %s." % option) 
        option = input(" ")
        equip()
    else:
        print ("You don't have %s in your inventory" % option) # tells the user they are trying to equip a weapon they do not have
        

def prefight(): # function that randomly decides which enemy the user will fight when they choose hunt in the tavern menu
    global enemy
    enemynum = random.randint(1, 2)
    if enemynum == 1:
        enemy = ogre
    else:
        enemy = giant
    fight() # calls the fight function
    
def fight(): # function that introduces the fight scene to the user
    print ("%s     vs      %s" % (player.name, enemy.name)) # displays the player's and the enemy's stats 
    print ("%s's Health: %d/%d    %s's Health: %i/%i" % (player.name, player.health, player.maxhealth, enemy.name, enemy.health, enemy.maxhealth))
    print ("1. Attack")
    print ("2. Run")
    option = input(' ')
    if option == "1": # logic statements that lets the user either attack or attempt to run
        attack()
    elif option == "2":
        run()
    else:
        fight()

def attack(): # function that determines the damage when the user chooses to attack
    PAttack = random.randint(int(player.attack/2), int(player.attack)) # randomly generates an attack value based off the attack of the current weapon
    EAttack = random.randint(int(enemy.attack / 2), int(enemy.attack))
    if PAttack == player.attack / 2: # there is a chance that the player may miss the attack
        print ("You miss!")
    else:
        enemy.health -= PAttack # substracts the attack damage from the enemy health
        print ("You deal %i damage!" % PAttack)
    option = input(' ')
    if enemy.health <=0:
        win() # if the player kills the enemy, calls the win function
    if EAttack == enemy.attack/2: # there is a chance that the enemy may miss the attack
        print ("The enemy missed!")
    else:
        player.health -= EAttack # substracts the attack damage from the player health
        print ("The enemy deals %i damage!" % EAttack)
    option = input(' ')
    if player.health <= 0:
        dead() # if the player dies, calls the dead function
    else:
        fight()

def run(): # function that allows the player to run from a fight
    runnum = random.randint(1, 3) # randomly generates a chance of being able to run away
    if runnum == 1:
        print ("You have successfully ran away!")
        option = input(' ')
        tavern() # takes the player back to the tavern
    else:
        print ("You failed to get away!")
        option = input(' ')
        EAttack = random.randint(int(enemy.attack / 2), int(enemy.attack))
        # if the player fails to get away, the enemy attacks the player
        if EAttack == enemy.attack/2:
            print ("The enemy missed!")
        else:
            player.health -= EAttack
            print ("The enemy deals %i damage!" % EAttack)
        option = input(' ')
        if player.health <= 0:
            dead() #calls the dead function
        else:
            fight() # calls the fight function to start the next fight turn

def win(): # function that is called when the player wins a fight
    enemy.health = enemy.maxhealth # resets the enemy's health for the next fight
    player.gold += enemy.goldgain # the player gains gold from killing the enemy
    print ("You have defeated the %s" % enemy.name)
    print ("You found %i gold!" % enemy.goldgain)
    option = input(' ')
    tavern() # returns the player to the tavern
    
def dead(): # function that is called when the player dies in battle
    print ("Your legend is over.")
    sys.exit() # exits the game
    option = input(' ')
    
def store(): # store function where the user can buy new weapons
    print ("Welcome traveller, I have wares, if you have coin")
    print ("\nEnter the name of the weapon you would like to buy\n")
    print ("1. Axe")
    print ("2. Crossbow")
    print ("3. Greatsword")
    print ("Back")
    print (" ")
    option = input(' ')
    # logic statements that determines if the user can buy the weapon
    if option in weapons:
        if player.gold >= weapons[option]:
            player.gold -= weapons[option] # if the player has enough gold to buy the weapon, the gold is subtracted from their total
            player.weap.append(option)
            print ("You have bought %s" % option)
            option = input(' ')
            store()
        
        else: # the player is told that they do not have enough gold, and sent back to the store menu
            print ("You don't have enough gold")
            option = input(' ')
            store()
    
    elif option == "Back":
        tavern() # returns the player back to the tavern
    
    else:
        print ("That item does not exist") # tells the user that theyve entered an invalid weapon name and sends them back to the store
        option = input(' ')
        store()
    
main() #calls the main function to start the code
