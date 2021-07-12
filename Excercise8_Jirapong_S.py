usernameInput = input("Username : ")
passwordInput = input("Password : ")
username = "jirapongs"
password = "Jirapong24"
if usernameInput == username and passwordInput == password :
    print("-"*6,"Welcome to iJirapong Shop","-"*6)
    print("My available products are shown below")
    applePrice = 45
    bananaPrice = 15
    computerPrice = 20000
    televisionPrice = 15000
    print("1","-","Apple",str(applePrice),"THB")
    print("2","-","Banana",str(bananaPrice),"THB")
    print("3","-","Computer",str(computerPrice),"THB")
    print("4","-","Television",str(televisionPrice),"THB")
    userSelected = input("Select the product name or number : ")
    qtySelected = int(input("Select the quantity : "))
    if userSelected == "Apple" or userSelected == "1" :
        totalPrice = applePrice*qtySelected
        print("Total price of Apple","x",str(qtySelected),":",totalPrice,"THB")
    elif userSelected == "Banana" or userSelected == "2" :
        totalPrice = bananaPrice*qtySelected
        print("Total price of Banana", "x", str(qtySelected), ":", totalPrice, "THB")
    elif userSelected == "Computer" or userSelected == "3" :
        totalPrice = computerPrice*qtySelected
        print("Total price of Computer","x",str(qtySelected),":",totalPrice,"THB")
    elif userSelected == "Television" or userSelected == "4" :
        totalPrice = televisionPrice*qtySelected
        print("Total price of Television","x",str(qtySelected),":",totalPrice,"THB")
    else :
        print("Sorry, Your selected product is not found")
    print("-"*6,"Thank you for shopping with us","-"*6)
else :
    print("Your username or password are incorrect")













































