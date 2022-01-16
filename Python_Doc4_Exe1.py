        #############################################################
        #                     Python Document 3                     #
        #         Shopping Cart - Object Oriented Programming       #
#############################################################################
# Program Objectives:                                                       #
# 1. Allow customers review products in a catalogue before adding them      #
#    in a shopping cart.                                                    #
# 2. Allow customers to manage their shopping cart contents.                #
# 3. Display shopping cart contents when requested.                         #
# 4. Clear console everytime a new action is selected.                      #
# 5. Administrative and financial actions are not part of this program.     #
#                                                                           #
# Program Structure Design:                                                 #
#                                                                           #
# 1. Blueprints:                                                            #
#        Class # 1: Main program - Shopping Cart. This class will contain   #
#                   all instances and methods necessary to complete a       #
#                   successful shopping event                               #
#        Class # 2: Driver program allowing users to select from a menu of  #
#                   of functions.                                           #
#        Class # 3: Products Catalogue contains available items and their   #
#                   prices per unit.                                        #
#                                                                           #
# 2. Driver Program to orchestrate the necessary functions to complete the  #
#    user's shopping event. The driver in this exercise acts also as the    #
#    users interface (see Class # 2) above.                                 #
#                                                                           #
# 3. Decorators:                                                            #
#    @classmethod: The purpose of this @classmethod is to allow it's class  #
#    to act as a driver and execute before the ShoppingCart instances       #
#    are created. They will be created once the user selects his            #
#    desired function.                                                      #
#                                                                           #
# Data Structure:                                                           #                                                                         #
# 1- Dictionary1: Contains user's purchased items (product name, quantity,  #
#    and price.                                                             #
# 2- Dictionary2: Contains catalogue items (product name, and price).       #
#############################################################################
#
import os,sys, file1
from textblob import TextBlob   # Make sure TextBlob package is installed first
#
class ShoppingCart():
    def __init__(self):
        self.cart = {}
        self.cart_balance = 0
        self.cart_count = 0

    #
    # Selection 2: View shopping cart
    #
    
    def displayCart(self):
        
        """ Screen Section Header """
        print("----------------------------------------")
        print("---- Viewing Shopping Cart Contents ----")
        print("----------------------------------------")

        self.cart_balance = 0
        self.cart_count = 0
        
        if len(ShopCart.getCart()) <= 0:
            print(f"\nTher are no items in your shopping cart." )    
        else:
            for x, y in self.cart.items():
                self.cart_count += y[0]
                self.cart_balance += y[1]
                # List each shopping item, item qty, and item price as bullets.
                print("- " + x, y)    
            
        print("Items count: ", round(self.cart_count))    
        print("Cart Balance: $", round(self.cart_balance,2))
        
        go_back = input(f"\nEnter 'm' to go back to main menu:  ").lower().strip()[0]
                
        if go_back == "m":
            os.system('cls')
            
    #
    # Selection 3: Add Add items to shopping cart
    #
    

    #def addItem(self, key_val, qty_val, price_val):
    def addItem(self, key_val="", qty_val=1, price_val=1):    
        
        """ Screen Section Header """
        print("---------------------------------------")
        print("---- Adding Items to Shopping Cart ----")
        print("---------------------------------------")
        print()                             # Blank line
        more_items = "y"
        # Enable users to add items and their quantities into shopping cart 
        while more_items == "y":
            add_item = input("\nEnter item to add: ").lower().strip()
            add_qty = int(input("Enter Quantity: ").strip())
            
            qty_val = add_qty
            key_val = add_item
            
            # Perform a dict key check to see if item is on shopping catalogue
            # imported file1 performs the check taking the dict_key & prod_cat dictionary as arguments, 
            """ When a shopping item is found in catalogue, file1 returns 3 outputs """
            """ When a shopping item is not found in catalogue, file1 returns 2 outputs """
            
            if len(file1.checkKey(key_val, dictionary)) == 3:
                
                """ Calculate the item total price """
                price_val = qty_val * dictionary[key_val]
            
                """ Add found item into the shopping cart """
                self.cart[key_val] = (qty_val, price_val)
                
                print(self.cart)
                print(key_val, " - added to your shopping cart!")
            else:
                print(key_val, " - not added to your shopping cart!")
                print("Try entering another item")
                
            # This code allows users to add more items without exiting to the main menu
            more_items = input("\nWould you like to add another item? Y/N ").lower().strip()[0]
            
        
    #
    # Selection 4: remove item is in shopping cart
    #
    
    def removeItem(self, key_val=""):
        
        """ Screen Section Header """
        print("----------------------------------------------------")
        print("---- Removing Items from Shopping Cart Contents ----")
        print("----------------------------------------------------")
        
        if len(ShopCart.getCart()) <= 0:
            print("Shopping cart is empty. This is selection is not available")
            
            go_back = input(f"\nEnter 'm' to go back to main menu:  ").lower().strip()[0]
                
            if go_back == "m":
                os.system('cls')
        else:
            del_item = input(f"\nEnter the item to remove from the cart: ")
            key_val = del_item
            
            if key_val in self.cart:
                del self.cart[key_val]
                print({del_item}, " has been removed from your cart")
            else:
                print({del_item}, " is not found in your cart")

    #
    # Selection 5: Check if item is in shopping cart
    #
    def checkItem(self):
        
        """ Screen Section Header """
        print("-----------------------------------------------")
        print("---- Checking Item Exists in Shopping Cart ----")
        print("-----------------------------------------------")

        check_item = input("What item do you wish to check in the cart: ")
        
        key_val = check_item
        
        if key_val in self.cart:    
            print(f"\n{check_item} is in your cart")
        else:    
            print (f"\n{check_item} does not exist. Check your spelling and try again!")
    
    #
    # Selection 6: Clear shopping cart
    #
    def emptyCart(self):
        self.cart.clear()
        print("Your cart has been cleared. View your cart to confirm.")

    #
    # Selection 7: Checkout and Exit
    #
    def checkOut(self):
        print("Currently, this option is not available.")
        self.cart.clear()
        sys.exit(f"\nExit is successful!")
    
    def getCart(self):
        return self.cart

class ShoppingCatalogue():
    def __init__(self, name, price):
        self.name = name.lower()
        self.price = price
        
#            
# This is user interface section - it's coded as a classmethod so it starts 
# before the preceeding instances. 
#
class Console():
    @classmethod
    def mainMenu(cls, ShopCart, prod_cat):
        os.system('cls')
        
        while True:
            # The program starts by displaying this Main Console before any
            # instances are created
            print(f"\n--- MAIN CONSOLE ---")      
            print("""### SHOPPING CART MENU ###

            Select your action option from the list below:

            1. Browse Products Catalogue
            2. View Shopping Cart
            3. Add Item To Shopping Cart
            4. Remove Item From Shopping Cart
            5. Check If Item Is In Shopping Cart
            6. Clear Items From Shopping Cart
            7. Checkout and Exit
            8. Exit
            """)
            
            # User selection from above action options
            selection = int(input("Enter your selection here: "))

            """ Option 1: Displays a list of products available for shoppers """
            if selection == 1:
                os.system('cls')
                
                """ Screen Section Header """
                print("-----------------------------------------------------------")
                print("------ Viewing Available Products Catalogue Contents ------")
                print("-----------------------------------------------------------")
                print(" ========================================================= ")
                print("|  Product      |   Price    |  Product      |   Price    |")
                print("|=========================================================|")
                print("| Onion         |       $0.54| grapes        |       $2.35|")
                print("| Garlic        |       $0.86| Strawberry    |       $3.45|")
                print("| Parsley       |       $0.57| Milk          |       $3.45|")
                print("| Kale          |       $1.10| Butter        |       $2.96|")
                print("| Celery        |       $0.97| Yogurt        |       $3.67|")
                print("| Carrot        |       $2.34| Eggs          |       $1.29|")
                print("| Tomato        |       $2.25| Cheese        |       $2.15|")
                print("| Beans         |       $1.23| Turkey        |       $1.59|")
                print("| Apple         |       $0.79| Ham           |       $0.99|")
                print("| Orange        |       $1.15| Chicken       |       $1.25|")
                print("| Banana        |       $0.46| Roast         |       $5.65|")
                print("| Melon         |       $3.46| Steak         |      $11.45|")
                print(" ========================================================= ")
                
                go_back = input(f"\nEnter 'm' to go back to main menu:  ").lower()[0]
                
                if go_back == "m":
                    os.system('cls')   
            #    
            elif selection == 2:
                os.system('cls')
                ShopCart.displayCart()
            #    
            elif selection == 3:
                os.system('cls')
                ShopCart.addItem()
            #    
            elif selection == 4:
                os.system('cls')
                ShopCart.removeItem()
            #    
            elif selection == 5:
                os.system('cls')
                ShopCart.checkItem()
            #    
            elif selection == 6:
                os.system('cls')
                ShopCart.emptyCart()
            #
            elif selection == 7:
                os.system('cls')
                ShopCart.checkOut()
            #
            elif selection == 8:
                os.system('cls')
                exit_response = input(f"\nYou've selected to exit. Are you sure? (Y/N):  ").lower()[0]
    
                if exit_response == "y":
                    sys.exit(f"\nExit is successful!")
                else:
                    print(f"\nYou've cancelled your exit")   
            else:
                print(f"\n {selection} is an invalid selection")

# This is the Driver Code section:
             
# Shopping Catalogue: Dictionary (item: price per unit)
prod_cat = {
    "onion": 0.54, "garlic": 0.86, "parsley": 0.57,
    "romaine": 0.57, "kale": 1.10, "celery": 0.97,
    "carrot": 2.34, "tomato": 2.25, "beans": 1.23,
    "apple": 0.79, "orange": 1.15, "banana": 0.46,
    "melon": 3.46, "grapes": 2.35, "strawberry": 3.45,
    "milk": 3.45, "butter": 2.96, "yogurt": 3.67,
    "eggs": 1.29, "cheese": 2.15, "Turkey": 1.59,
    "Ham": 0.99, "chicken": 1.25, "Roast": 5.65,
    "steak": 11.45 
}

dictionary = prod_cat
ShopCart = ShoppingCart()
#
Console.mainMenu(ShopCart, prod_cat)