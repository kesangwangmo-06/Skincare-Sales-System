def generate_invoice(file_path, name, phone_number, datetime_now, items, shipping_cost, grand_total):
    """
    Writes a customer purchase invoice to a text file.

    Parameters:
        file_path (str): Path to the invoice file.
        name (str): Customer's name.
        phone_number (str): Customer's contact number.
        datetime_now (datetime): Date and time of purchase.
        items (list): List of purchased items as tuples (item_name, quantity, unit_price, total, free_qty).
        shipping_cost (int): Cost of shipping if applicable.
        grand_total (int): Total amount after shipping.

    Example:
        generate_invoice("invoice.txt", "Dolma Lama", "9876543210", datetime.now(),
                         [("eye cream", 2, 500, 1000, 0)], 50, 1050)
    """
    file = open(file_path, "a")#opens the file in append mode
    file.write("\n" + "="*100 + "\n")
    file.write("\t\t\tWe Care\n")
    file.write("\t\tBoudha, Kathmandu | Phone No: 9841277311\n")
    file.write("-------------------------------------------------------------------------\n")
    file.write("Customer Details:\n")
    file.write("-------------------------------------------------------------------------\n")
    file.write("Name of the Customer: " + name + "\n")
    file.write("Contact number: " + phone_number + "\n")
    file.write("Date and time of purchase: " + str(datetime_now) + "\n")
    file.write("-------------------------------------------------------------------------\n")
    file.write("\nPurchase Detail:\n")
    file.write("------------------------------------------------------------------------------------------------------------------\n")
    file.write("Item Name \t Quantity \t Free \t Unit Price \t Total\n")
    file.write("------------------------------------------------------------------------------------------------------------------\n")
    #write each purchased items details in thew file
    for item in items:
        file.write(item[0] + "\t" + str(item[1]) + "\t\t" + str(item[4]) + "\t\t" + str(item[2]) + "\t\t$" + str(item[3]) + "\n")
    file.write("------------------------------------------------------------------------------------------------------------------\n")
    #shipping cose if applicable
    if shipping_cost > 0:
        file.write("Shipping Cost: $" + str(shipping_cost) + "\n")
    #add the final total
    file.write("Grand Total: $" + str(grand_total) + "\n")
    file.close()


def restock_invoice(file_path, restock_records, datetime_now):
    """
    Appends a summary of restocked items to a text file.

    Parameters:
        file_path (str): Path to the restock invoice file.
        restock_records (list): List of restocked product details as tuples (product_name, added_qty, total_qty, price).
        datetime_now (datetime): Date and time of the restock.

    Example:
        restock_invoice("restock.txt", [("Eye Cream", 10, 30, 550)], datetime.now())
    """
    with open(file_path, "a") as file:
        file.write("\n" + "="*100 + "\n")
        file.write("\t\t\tWe Care - Restock Invoice\n")
        file.write("\t\tBoudha, Kathmandu | Phone No: 9841277311\n")
        file.write("-------------------------------------------------------------------------\n")
        file.write("Admin Restock Summary:\n")
        file.write("-------------------------------------------------------------------------\n")
        #write deails for restock products
        for record in restock_records:
            file.write("Product: " + record[0] + "\n")
            file.write("Quantity Added: " + str(record[1]) + "\n")
            file.write("New Total Quantity: " + str(record[2]) + "\n")
            file.write("Updated Price: $" + str(record[3]) + "\n")
            file.write("-------------------------------------------------------------------------\n")
        #add time stamp for the restock
        file.write("Restocked on: " + str(datetime_now) + "\n")
        file.write("="*100 + "\n")
