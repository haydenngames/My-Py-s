buisness1 = "buisness"
buisness1type = "buisnesstype"
buisness2 = "buisness"
buisness2type = "buisnesstype"
buisness3 = "buisness"
buisness3type = "buisnesstype"

print("Welcome to the buisness life there is endless opertunitys you will never know what couled happen...")
print("when we say endless i mean endless you yourself could create the zombie apocalips. only if your an idiot")
print("But i know your not. am i right?")
right = input("(yes/no) --> ")

if right == "yes":
    print("Oh thank got. i new i could trused you.")

if right == "no":
    print("oh. ill protend i dident here that.")

print("anyway. lest start you first buisness.")
print("what sort of buisness would you like to own:")
print("1.street shop")
print("2.cafe")
print("3.factory")


bstype = input("--> ")


if bstype == "1":
    buisness1type = "street shop"
    print("you have started a", buisness1type)

if bstype == "2":
    buisness1type = "cafe"
    print("you have started a", buisness1type)

if bstype == "3":
    buisness1type = "factory"
    print("you have started a", buisness1type)

print("Now you have started your buisness")
print("What would you like to call your", buisness1type)

bsname = input("Name -->")


buisness1 = bsname

print("ok. you now own a", buisness1type, "named", buisness1)
print("you will need some product go to the market on the laptop")