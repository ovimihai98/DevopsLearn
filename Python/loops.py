#For Loop
"""
PLANET = "Earth"

for i in PLANET:
    print(i)
print("Rest of the code.")
"""

#While Loop

"""
x = 0
while x <= 10:
    print("Value of x is:", x)
    print("Looping")
    x+=1

print("Rest of the code")
"""

#Nested Loop
"""
ANIMALS = ["Dog", "Cow", "Rooster", "Sheep", "Pig", "Cat"]

for animal in ANIMALS:
    print("")
    print(f"I will spell {animal} for you:")
    for letter in animal:
        print(letter)
"""
import time
x = 2
while True:
    print("Value of x is:", x)
    print("Looping")
    x*=2
    time.sleep(0.5)
