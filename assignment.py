from datetime import datetime
from assignment1 import write_invoice


# Making an empty dictionary to store product data
product_data = {}
file = open("data.txt", "r")
ff = file.readlines()
item_id = 1
for data in ff:
    data = data.replace("\n", "").split(",")
    product_data[item_id] = data
    item_id += 1
file.close()

# Display product data
print()
for key, value in product_data.items():
    print(key, ":", value)

print("-" * 80)
print("ID \t Product \t brand \t\t price \t qty \t country")
print("-" * 80)
for key, value in product_data.items():
    print(key, end="\t")
    for each in value:
        print(each, end="\t")
    print()
print("-" * 80)
#main loop for admin operation
main_loop = True
while main_loop:
    print(" 1. Purchase")
    print(" 2. Restock a product")
    print(" 3. Exit the application")

    choice = int(input("Enter the option to continue: "))
    print("\n")

    if choice == 1:
        #collecting customer details
        print("Enter your details to generate the bill:")
        name = input("Please enter the name of the customer: ")
        phone_number = input("Please enter the phone number of the customer: ")
        purchased_items = []
        grand_total = 0
        shipping_cost = 0
        total = 0

        #asking for product id and quantity
        while True:
            try:
                product_id=int(input("Enter the ID of the product you want to purchase:"))
                if 1<= product_id <= len(product_data):
                    break
                else:
                    print("Invalid product ID. please try again")
            except ValueError:
                print("Please enter a valid ID")

        while True:
            try:
                product_quantity=int(input("please provide the quantity you want to buy:"))
                qty_r=product_data[product_id][2]
                free_qty=product_quantity //3
                total_deduct=product_quantity+ free_qty

                if product_quantity >0 and total_deduct <= int(qty_r):
                    break
                else:
                    print("The quantity is not available")
            except ValueError:
                print("Invalid quantity")
                
                    
        #informing customer about offer
        print("\nDear", name, "you received", free_qty, "items for free as part of the offer.")
        #update stock
        product_data[product_id][2] = str(int(product_data[product_id][2])- total_deduct)

        # Calculating total price
        product_name = product_data[product_id][0]
        unit_price = int(product_data[product_id][3]) * 2
        total_price = unit_price * product_quantity

        purchased_items.append([product_name, product_quantity, unit_price, total_price, free_qty])
        total += total_price
        #shipping option
        shipping_choice = input("Do you want your products to be shipped? (Y/N): ").lower()
        if shipping_choice == "y":
            shipping_cost = 500

        grand_total = total + shipping_cost
        today_date_and_time = datetime.now()

        # Writing updated stock to file
        with open("data.txt", "w") as file:
            for values in product_data.values():
                file.write(",".join(values) + "\n")

        # Printing bill 
        print("\t\t\tWe Care \n")
        print("\t\tBoudha, Kathmandu | Phone No: 9841277311\n")
        print("-------------------------------------------------------------------------")
        print("Customer Info:")
        print("-------------------------------------------------------------------------")
        print("Name of the Customer:", name)
        print("Contact number:", phone_number)
        print("Date and time of purchase:", str(today_date_and_time))
        print("-------------------------------------------------------------------------")
        print("\nPurchase Detail:")
        print("------------------------------------------------------------------------------------------------------------------")
        print("Item Name \t\t Quantity \t Free \t Unit Price \t Total")
        print("------------------------------------------------------------------------------------------------------------------")
        for i in purchased_items:
            print(i[0] + "\t\t" + str(i[1]) + "\t\t" + str(i[4]) + "\t" + str(i[2]) + "\t\t$" + str(i[3]))
        print("------------------------------------------------------------------------------------------------------------------")
        if shipping_cost > 0:
            print("Shipping Cost: $" + str(shipping_cost))
        print("Grand Total: $" + str(grand_total))
        print("\n")
        #saving invoice to file
        write_invoice("assignment1.txt", name, phone_number, today_date_and_time, purchased_items, shipping_cost, grand_total)


    elif choice == 2:
        #restocking selected products
        print("Restocking the products")
        for key, value in product_data.items():
            print(str(key) + ". " + value[0] + " (Quantity: " + value[2] + ", Cost Price: " + value[3] + ")")
        restock_id = int(input("Enter the ID of the product to restock: "))
        if restock_id in product_data:
            qtyy = int(input("Enter quantity to add: "))
            cost = input("Enter new price: ")
            product_data[restock_id][2] = str(int(product_data[restock_id][2]) + qtyy)
            if cost: 
                product_data[restock_id][3] = cost
            with open("data.txt", "w") as file:
                for values in product_data.values():
                    file.write(",".join(values) + "\n")
            print("Product restocked successfully!")
        else:
            print("Invalid Product ID.")

    elif choice == 3:
        #exiting the system
        main_loop = False
        print("Thank you for using the system\n")

    else:
        #invalid menu option
        print("Your option", choice, "is invalid \n")
