#Pokemon Damage Calculator

import random
import sys

print("\n                    ~~-----Pokemon Damage Calculator-----~~\n")

#Pokemon Level
print("Level of the Attacking Pokemon: ")
level = int(input())
#Pokemon Special Attack
print("\nSpecial Attack of the attacking Pokemon: ")
sa = float(input())
#Pokemon Special Defense
print("\nSpecial Defense of the defending Pokemon: ")
sd = float(input())
#Pokemon Power
print("\nPower of the attacking Pokemon move used: ")
power = float(input())
#Initial Damage w/o Modifier
damage = (((2 * level / 5 + 2) * (power * sa / sd)) / 50 + 2)
print("\nInitial Damage is, ",damage)

#Modifiers

random1 = round(random.uniform(.85, 1.00),2)
print("\nRandom number between .85 and 1.00:")
print(random1)

print("\nTargets: ")
targets = float(input())
if targets >=2:
    targets = (0.5)
else:
    targets = (1)
print("Target Value: ")
print(targets)
print("\nWeather: ")
weather = float(input())

print("\nBadge: ")
badge = float(input())

print("\nCritical(Yes/No): ")
critical = str(input())
yes = "Yes" 
no = "No"
if critical == yes:
    critical = float(2)
elif critical == no:
    critical = float(1)
else:
    print("Please choose the correct input(Yes/No)")

        
print("\nstab: ")
stab = float(input())

print("\ntype: ")
type1 = float(input())

print("\nburn: ")
burn = float(input())

#Final Damage w/ Modifier
modifier = targets * weather * badge * critical * random1 * stab * type1 * burn
damage_mod = damage * modifier
print("\n\nFinal Damage is, ",round(damage_mod,2))
print("\n")