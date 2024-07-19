'''
In this make task we will write a program that simulates an encounter with a zombie in an RPG. 
To this end, you should first create a list of possible weapons. 
Second you should create a variable zombieWeakness that is randomly assigned to one of the weapons in you list. 
Output a message telling the user that they have encountered a zombie and should prepare to fight. 
Output the list of weapons to the user.  Ask if they want to type 1 to use a random weapon from the list or 2 to pick their own weapon. 
If the weapon picked matches the zombieWeakness, output a message telling the user that they have won the fight.  
Otherwise output a message saying that they have lost.
'''

import random

weapons = ['Flamethrower', 'Bat', 'Knife', 'Gun', 'Taurus', 'Revolver'] # Create list of available weapons

zombieWeaknesses = random.choices(weapons, k=int(len(weapons)/2)) # Select a subset of the list as zombie weaknesses (extension to original task)

print('You encountered a zombie. Get ready to fight!!!')
print("You have the following weapons available:")
for i in range(len(weapons)):
    availableWeapon = weapons[i]
    print(f'{i}: {availableWeapon}')

choice = int(input("Press 1 to select a random weapon and 2 to select manual\n"))

if choice == 1:
    weapon = random.choice(weapons)
elif choice == 2:
    weaponIndex = int(input("Select the index of a weapon:\n>"))
    weapon = weapons[weaponIndex]
else:
    print("Invalid option")

if weapon in zombieWeaknesses:
    print(f"You choose: {weapon}")
    print(f"Zombie weaknesses: {zombieWeaknesses}")
    print("You won")
else:
    print(f"You choose: {weapon}")
    print(f"Zombie weakness: {zombieWeaknesses}")
    print("You loose")