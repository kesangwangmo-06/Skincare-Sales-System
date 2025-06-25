#loads data from the text file and stores it in a dictionary
def load_data():
    """
        Loads product data from a text file into a dictionary.

    Returns:
        dict: A dictionary where the product ID is the key and the product details are the value.

    Example:
        product_data = load_data()
    """
    product_data = {} #creates an empty dictionary
    file = open("data.txt", "r")#opens the file in read mode
    ff = file.readlines()#read all the lines from the file

    item_id = 1
    for data in ff:
        data = data.replace("\n", "").split(",")
        product_data[item_id] = data
        item_id += 1#move to the next id
        
    file.close()
    return product_data #returns the complete dictionary
