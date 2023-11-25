# Variable Length Argumets(Non Keyword Arguments)
"""
def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
    for item in args:
        print(f"You have ordered : {item}")
    print("Your food will be delivered in 30 mins")
    print("Enjoy the party")

order_food("Salad", "Pizza", "Burgers", "Soup")
"""

import random
def time_activity(*args,**kwargs):
    '''
    Input: Multiple values for minutes, key=value pair activity
    Output: Return sum of minutes + random minute spend on a random acitivty
    '''
    #print(args)
    #print(kwargs)
    min = sum(args) + random.randint(0, 60)
    #print(min)
    choice = random.choice(list(kwargs.keys()))
    #print(choice)
    print(f"You have to spend {min} minutes for {kwargs[choice]}.")


time_activity(10, 20, 10, hobby="Dancing", sport="Boxing", fun="Driving", work="DevOps learning")
