"""
This script will implement our knowledge of
conditions and different datatypes
"""

print("This IT Organization has various skill sets.")
print("Find out your match.")

print("Enter Capitalised Values: ")

DevOps = ["Jenkins", "Ansible", "Bash", "Puppet", "Dockers", "Kubernetes", "Terraform"]
Development = ("NodeJs", "AngularJs", "Java", ".net", "Python")
cntr_empl1 = {"Name":"Santa", "Skill":"Blockchain", "Code":1024}
cntr_empl2 = {"Name":"Rocky", "Skill":"AI", "Code":1218}

usr_skill = input("Enter your desired skill: ")
#Check skill
if usr_skill in DevOps:
    print(f"We Have {usr_skill} in DevOps Team.")
elif usr_skill in Development:
    print(f"We have {usr_skill} in Development Team.")
elif usr_skill in cntr_empl1.values() or usr_skill in cntr_empl2.values():
    print(f"We have contract employees with {usr_skill}.")
else:
    print("Skill not found")
    print("Please check if you have entered value in capitalize or check spelling")
