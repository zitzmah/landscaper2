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
            break
    win()

def upgrade():
    print("you chose to upgrade")
    player["weapon"] += 1
    print(weapons[player["weapon"]])

def quitGame():
    print("game ends")

def win():
    getInput()

getInput()