planet1 = "Closest to the Sun"
print(planet1)

print(planet1[0])
print(planet1[1])
print(planet1[2])

print(planet1[-1])
print(planet1[-2])
print(planet1[-3])

#Slicing a string, get a substring from a string
print(planet1[1:4])
print(planet1[:7])
print(planet1[15:])

#Slicing tuple
devops = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")
print(devops[0])
print(devops[4])
print(devops[-1])
print(devops[2:5])
print(devops[2:5][0])
print(devops[2:5][0][5:11])

#Dictionary Example

Skills = {"DevOps": ("AWS", "Jenkins", "Python", "Ansible"), "Development": ["Java", "NodeJS", ".NET"]}
print(Skills)
print(Skills["DevOps"])
print(Skills["Development"])
print(Skills["DevOps"][-1])
print(Skills["DevOps"][-1][:3])
