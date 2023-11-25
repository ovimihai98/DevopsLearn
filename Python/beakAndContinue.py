#Break
"""
for i in "devops":
    print(i)
    if i == "o":
        print("Found my data")
        break
print("out of loop")
"""
#Continue

for i in "devops":
    if i == "o":
        print("Found my data")
        continue
    print(i)
print("out of loop")