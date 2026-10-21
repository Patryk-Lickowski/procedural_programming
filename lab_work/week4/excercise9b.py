def vending_machine(balance):
    products = {
        1: {"name": "Crisps", "price": 100},
        2: {"name": "Chocolate", "price": 150},
        3: {"name": "Water", "price": 120}
    }

    print(f"Welcome to the Vending Machine! \nYour balance is {balance}p\n")
    for product_id, details in products.items():
        print(f"{product_id}. {details['name']} - {details['price']}p")
    next_id = max(products) + 1
    print(f"{next_id}. Quit\n")

    selection = int(input("Please select an option: "))
    if selection in products:
        if balance - products[selection]["price"] < 0:
            print("Insufficient balance")
            vending_machine(balance)
        else:
            balance -= products[selection]["price"]
            print(f"Purchase successful: {products[selection]["name"]} - Price: {products[selection]["price"]}p")
            vending_machine(balance)
    elif selection == next_id:
        print("Thank you for using the vending machine!")
    else:
        print("Invalid selection")
        vending_machine(balance)




vending_machine(200)
