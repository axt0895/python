#Shopping cart project

#intialize an empty dictionary as a shopping cart list
shopping_cart = {}


#Function to add items in shopping cart
def add_item_to_cart(item, price, quantity):
    if item in shopping_cart:
        shopping_cart[item] +=1
    else:
        shopping_cart[item] = quantity
        
def view_cart():
    print('\nShopping Cart')
    for item, quantity in shopping_cart.items():
        print('f{item}: {quantity} items')
    
def calculate_total():
    item_cost = 0
    item_prices = {
        "apple": 1.0,
        "banana": 0.5,
        "orange": 0.75,
        "bread": 2.5,
        "milk": 1.8
    }
    
while True:
    print('\n Select the operaion')
    print('1. Add an item to the cart')
    print('2. View cart')
    print('3. Calculate the total cost')
    print('4. Exit')
    
    user_input = input('Enter the choice (1/2/3/4): ')
    
    if user_input == '1':
        item_name = input('Enter the item name: ')
        item_price = float(input('Enter the item price: '))
        item_quantity = int(input('Enter the item quantity: '))
        add_item_to_cart(item_name, item_price, item_quantity)
        print(f'{item_quantity} items of {item_name} added to cart having price {item_price}')
        
    elif user_input == '2':
        view_cart()
        
    elif user_input == '3':
        total_cost = calculate_total()
        
    elif user_input == '4':
        print('Exiting the program')
        break
    else:
        print('Exiting the program')
        break