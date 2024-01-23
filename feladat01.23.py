import os, random

os.system("clear")

#2 ország közti lakosságszám különbség
def kolunbseg(orsz1, orsz2):
    #1. megoldás:
    """if(orsz1>orsz2):
        return orsz1-orsz2
      else:
        teturn orsz2-orsz1"""
    #2. megoldás:
    return abs(orsz1-orsz2)

#2 orszég lakosság száma (8-20 millió között)
o1=random.randrange(8, 21)
o2=random.randrange(8, 21)

print("1. ország: ", o1, "millió fő")
print("2. orszég: ", o2, "millió fő")
print("")