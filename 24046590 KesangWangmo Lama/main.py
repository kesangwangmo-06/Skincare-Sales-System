from datetime import datetime
from read import load_data
from write import generate_invoice
from write import restock_invoice
from operations import *

#start the main loop for the application
main_loop = True

while main_loop:
    #load product data from file
    product_data = load_data()

    print()
    #display product data
    for key, value in product_data.items():
        print(key, ":", value)

    print("-" * 80)
    print("ID \t Product \t brand \t\t qty \t price \t country")
    print("-" * 80)
    for key, value in product_data.items():
        print(str(key) + "\t" + value[0] + "\t" + value[1] + "\t" + value[2] + "\t" + value[3] + "\t" + value[4])

    print("-" * 80)

    #show main menu options
    print(" 1. Purchase")
    print(" 2. Restock a product")
    print(" 3. Exit the application")

    #get users menu choice
    choice = get_menu()
    print("\n")

    if choice == 1:
        show_products(product_data)

        #get customers details
        print("Enter your details to generate the bill:")
        name = input("Please enter the name of the customer: ")
        phone_number = input("Please enter the phone number of the customer: ")

        #initialize purchase values
        purchased_items = []
        total = 0
        shipping_cost = 0
        grand_total = 0

        #loop to allow multiple purchases

        while True:
            product_id = get_product_id(product_data)
            qty_available = int(product_data[product_id][2])
            product_quantity, free_qty = get_purchase_qty(qty_available)

            print("\nDear", name, "you received", free_qty, "items for free as part of the offer.")

            #update stock
            product_data[product_id][2] = str(qty_available - product_quantity - free_qty)

            #calculate cost and rscord purchase
            product_name = product_data[product_id][0]
            unit_price = int(product_data[product_id][3]) * 2
            total_price = unit_price * product_quantity

            purchased_items.append([product_name, product_quantity, unit_price, total_price, free_qty])
            total += total_price

            #ask if user wants to buy more
            more = input("Do you want to buy another item? (Y/N): ").lower()
            if more not in ['y', 'yes']:
                break

            #ask for shipping

        shipping_choice = input("Do you want your products to be shipped? (Y/N): ").lower()
        if shipping_choice == "y":
            shipping_cost = 500

        #calculating final total
        grand_total = total + shipping_cost
        today_date_and_time = datetime.now()

        #saving updated stock
        save_data(product_data)

        #display bill on the screen
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

        #save invoice to file
        filename = "invoice_" + str(today_date_and_time).replace(":", "-").replace(" ", "_") + ".txt"
        generate_invoice(filename, name, phone_number, today_date_and_time, purchased_items, shipping_cost, grand_total)

    elif choice == 2:
        print("Restocking the products")
        restock_records = []

        #loop for multiple restocks
        while True:
            show_products(product_data)
            restock_id = get_product_id(product_data)
            qty = get_restock_qty()
            cost = input("Enter new price: ")

            #update product quantity and price
            product_data[restock_id][2] = str(int(product_data[restock_id][2]) + qty)
            if cost:
                product_data[restock_id][3] = cost
            save_data(product_data)
            print("Product restocked successfully!")

            #record restock details
            restock_records.append([product_data[restock_id][0], qty, product_data[restock_id][2], product_data[restock_id][3]])

            more=input("Do you want to restock another product?(Y/N):").lower()
            if more=="y":
                continue
            else:
                break
            
        today_date_and_time = datetime.now()
        filename = "restock_invoice_" + str(today_date_and_time).replace(":", "-").replace(" ", "_") + ".txt"
        restock_invoice(filename, restock_records, today_date_and_time)

        #displaying invoice on the screen
        print("\n" + "="*100)
        print("\t\t\tWe Care - Restock Invoice")
        print("\t\tBoudha, Kathmandu | Phone No: 9841277311")
        print("-------------------------------------------------------------------------")
        print("Admin Restock Summary:")
        print("-------------------------------------------------------------------------")
        for record in restock_records:
            print("Product:", record[0])
            print("Quantity Added:", record[1])
            print("New Total Quantity:", record[2])
            print("Updated Price: $", record[3])
            print("-------------------------------------------------------------------------")
                
    #if user selects 3
    elif choice == 3:
        main_loop = False
        print("Thank you for using the system\n")
