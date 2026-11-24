#make inventory of items
menu = ["iced coffee", "latte", "hot tea", "apple cider", "croissant", "brownie", "bagel"]
#empty money inventory
money = []

def wallet():
    """This function asks for user money amount and updates wallet"""
    #ask user for amoutj of money they have, store that in money index
    money= int(input("Please enter how much money you have (no special symbols needed): "))
    print("You currently have",money, "dollars!")
    
    """This function asks user what they would like to buy, user selects an item from the menu,
the menu inventory is updated."""
    # I need to also figure out how to assign values
    #(prices) to each item in the menu, and then update
    #how much money the user has left
    
def order():
    #ask user what they would like to buy
    user_input = input("What would you like to buy? (q to quit): ")

    while (user_input != "q" and user_input in menu):
        
        #check if item is in stock
        if user_input in menu:
            menu.remove(user_input)
            print(f"Here is your {user_input}! Enjoy!")
        #if item is already selected or out of stock, 
        else:
            print(f"So sorry, we are all out of {user_input}")
            print(f"Come back tomorrow and we'll have your order ready")
        
        print(f"Remaining inventory: {menu}\n")
    #fix the formatting here and make sure user can still buy items
    user_input = input("What would you like to buy next? (q to quit): ")


def main():
    #welcome statement here
    print("Welcome to Langley's Coffee Shop!")
    
    #call functions below
    wallet()
    order()

if __name__ == "__main__":
    main()