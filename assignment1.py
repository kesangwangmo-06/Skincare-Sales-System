# assignment1.py

def write_invoice(file_path, name, phone_number, datetime_now, items, shipping_cost, grand_total):
    with open(file_path, "a") as file:
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
        for item in items:
            file.write(item[0] + "\t" + str(item[1]) + "\t\t" + str(item[4]) + "\t\t" + str(item[2]) + "\t\t$" + str(item[3]) + "\n")
        file.write("------------------------------------------------------------------------------------------------------------------\n")
        if shipping_cost > 0:
            file.write("Shipping Cost: $" + str(shipping_cost) + "\n")
        file.write("Grand Total: $" + str(grand_total) + "\n")
