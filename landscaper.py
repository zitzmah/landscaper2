player = {
    "money": 0,
    "weapon": "teeth"
}

##Weapons list
weapons = [
    {"name": "teeth", "price":0, "money":1},
    {"name": "rusty scissors", "price":5, "money":5},
    {"name": "old lawnmower", "price":25, "money":50},
    {"name": "fancy lawnmower", "price":250, "money":100},
    {"name": "starving students", "price":500, "money":250},
]

def getInput():
    result = input("do you want to [w]ork [u]pgrade or [q]uit")

    if(result == "w"):
        work()
        return 1

    if(result == "u"):
        upgrade()
        return 1

    if(result == "q"):
        quitGame()
        return 1

    print("no valid options given")
    getInput()

def work():
    print("you chose to work today")
    weapon_name = player["weapon"]
    for weapon in weapons:
        if weapon["name"] == weapon_name:
            player["money"] += weapon["money"]
            print("you earned $",weapon["money"], "you now have $", player["money"])
    win()

def upgrade():
    print("you chose to upgrade")
    weapon_name = player["weapon"]
    for i in range(len(weapons)):
        if weapons[i]["name"] == weapon_name:
            if i+1 < len(weapons):
                if player["money"] >= weapons[i+1]["price"]:
                    player["weapon"] = weapons[i+1]["name"]
                    player["money"] -= weapons[i+1]["price"]
                    print("you upgraded to using",player["weapon"], "and you have $", player["money"])
                    getInput()
                else:
                    print("you don't have enough money to upgrade to ", weapons[i+1]["name"])
                    getInput()
            else:
                print("you already have the best tools available")
                getInput()

def quitGame():
    print("game ends")

def win():
    weapon_name = player["weapon"]
    if weapon_name == "starving students" and player["money"] >= 1000:
        print("you win!")
        quitGame()
    else:
        getInput()

getInput()