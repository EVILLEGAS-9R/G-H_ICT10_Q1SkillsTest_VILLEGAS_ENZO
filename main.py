from pyscript import display, document

def create_order(e):

    name = document.getElementById("cust_name").value
    address = document.getElementById("cust_address").value
    contact = document.getElementById("cust_contact").value


    total = 0
    items = ""

   
    if document.getElementById("nan_tea").checked:
        items += "Nan Tea, "
        total += 85.00

    if document.getElementById("caramel_macchiato").checked:
        items += "Caramel Macchiato, "
        total += 99.99

    if document.getElementById("red_velvet_cake").checked:
        items += "Red Velvet Cake, "
        total += 350.00

    if document.getElementById("iced_tea").checked:
        items += "Iced Tea, "
        total += 70.00

    if document.getElementById("sparkling_water").checked:
        items += "Sparkling Water, "
        total += 40.00

  
    if items == "":
        items = "No items selected"
    else:
        items = items[:-2] 


    document.getElementById("output").innerHTML = ""

   
    order_summary = f"""
    Order Summary
    
    Name: {name}
    Address: {address}
    Contact: {contact}

    Items Ordered: {items}

    Total Amount: ₱{total:.2f}
    """

    display(order_summary, target="output")
