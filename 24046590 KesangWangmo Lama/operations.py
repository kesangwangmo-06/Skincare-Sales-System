# function to display products
def show_products(product_data):
    """
        Displays the list of available products with ID, quantity, and price.

    Parameters:
        product_data (dict): Dictionary containing product information.

    Example:
        show_products(product_data)
    """
    print("\nAvailable Products:")
    for key, value in product_data.items():
        print(str(key) + ". " + value[0] + " (Quantity: " + value[2] + ", Cost Price: " + value[3] + ")")

#funciton to get and validate users main menu option
def get_menu():
    """
        Prompts and validates the user's main menu selection.

    Returns:
        int: The valid menu option chosen by the user (1, 2, or 3).

    Example:
        option = get_menu()
    """
    while True:
        try:
            choice = int(input("Enter the option to continue: "))
            if choice == 1 or choice == 2 or choice == 3:
                return choice
            else:
                print("Please choose 1, 2, or 3.")
        except:
            print("Invalid input. Please enter a number.")

#function to get and validate the product ID from the user
def get_product_id(product_data):
    """
    Prompts the user to enter a valid product ID.

    Parameters:
        product_data (dict): Dictionary of products.

    Returns:
        int: A valid product ID from the list.

    Example:
        product_id = get_product_id(product_data)
    """
    while True:
        try:
            product_id = int(input("Enter the ID of the product: "))
            if product_id >= 1 and product_id <= len(product_data):
                return product_id
            else:
                print("Product not available. Please try again")
        except:
            print("Please enter a valid ID")

#Function to get and validate quantity for purchase
def get_purchase_qty(available_qty):
    """
    Gets and validates quantity for purchase and calculates free items.

    Parameters:
        available_qty (int): Quantity available in stock.

    Returns:
        tuple: (purchase quantity, free items)

    Example:
        qty, free = get_purchase_qty(available_qty)
    """
    while True:
        try:
            quantity = int(input("please provide the quantity you want to buy:"))
            free = quantity // 3
            total_needed = quantity + free
            if quantity > 0 and total_needed <= available_qty:
                return quantity, free
            else:
                print("The quantity is not available")
        except:
            print("Invalid quantity")

#function to get and validate restock quantity from the user
def get_restock_qty():
    """
    Prompts the user to enter a valid restock quantity.

    Returns:
        int: Valid restock quantity.

    Example:
        qty = get_restock_qty()
    """
    while True:
        try:
            qty = int(input("Enter quantity to add: "))
            if qty > 0:
                return qty
            else:
                print("Quantity must be greater than 0.")
        except:
            print("Invalid input. Enter a valid number.")

#function to save the updated product data back to the file
def save_data(product_data):
    file = open("data.txt", "w")
    for values in product_data.values():
        file.write(",".join(values) + "\n")
    file.close()
