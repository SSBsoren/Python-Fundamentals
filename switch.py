def switch_roll(rollno):
    switcher={
        1:"Raju",
        2:"Avishek",
        3:"Sagen",
        4:"Ajay",
        }
    return switcher.get(rollno,"Invalid")
print(switch_roll(3))