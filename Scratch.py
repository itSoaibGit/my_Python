#Python CS50
name = input("What's your name?\n").strip().title()
first, middle, last = name.split()

ego = input(f"So your name is {last}?\n")

if ego == "Say my full name":
    print("Shut the fuck up!")
else:
    print("I see!")

for x in range (3):
    print("Soaib")