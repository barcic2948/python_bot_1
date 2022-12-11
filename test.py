target = "5D10"
target = target.replace(" ", "").lower()

if not target.find("d"):
    print("Cuj")

if not target.find("+"):
    bonus = 0

number = target[0: target.find("d")]
sides = target[target.find("d") + 1: target.find("+")]
bonus = target[target.find("+") + 1:]

print(number)
print(sides)
print(bonus)
