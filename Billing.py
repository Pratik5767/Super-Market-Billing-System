def addItem() :
    itemName = input("Enter the Item Name: ")
    itemPrice = int(input("Enter Item Price: "))
    itemQuat = int(input("Ente the Total Quantity: "))

    items = {"Name": itemName, "Price": itemPrice, "Quantity": itemQuat}
    store.append(items)
    print()
    print("Item Added Successfully")


def printBill():
    userItem = input("Enter Selling Item: ")
    userQuant = int(input("Enter Quantity: "))
    isFound = False

    for i in store:
        if userItem == i["Name"] and userQuant <= i["Quantity"]:
            isFound = True
            i["Quantity"] = i["Quantity"] - userQuant
            print("Remaning Quantity: ", i["Quantity"])
            totalBill = i["Price"] * userQuant
            print("Total Bill: ", totalBill)
            break

    if isFound == False:
        print()
        print("Item not available")


store = []

while True:
    print("1. Add Items")
    print("2. Print Bill")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    print()

    if choice == 1:
        addItem()
        print()
    elif choice == 2:
        printBill()
        print()
    elif choice == 3:
        print("Good Bye!!")
        break
    else:
        print("Invalid Input!!")
        print()