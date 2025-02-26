menu = {"Pizza":1.99, "Soda":0.69, "Double Chunk Chocolate Chip Cookie":2.49}
item = input("What would you like to add to the menu? \n")     
price = input("How much will your new item cost? \n")

def menuadd(item,price):
    menu[item] = price
    print("Your new menu is ", menu)

menuadd(item,price)