groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]

while True:
    yuck = input("What item would you like to remove from the grocery list? (Type 'stop' when you are done.)") 
    if yuck == "stop":
        print("Your new grocery list is: ", groceries)
        break
    groceries.remove(yuck)