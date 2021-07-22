def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    username = "jirapongs"
    password = "Jirapong24"
    if usernameInput == username and passwordInput == password:
        return True
    else:
        return False
def showMenu():
    print("Welcome !!!")
    print("-" * 3, "Jirapong.Shop", "-" * 3)
    print("Please select the calculator list")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def selectMenu():
    userSelected = int(input("Choose --> "))
    return userSelected
def vatCalculate(totalPrice):
    vat = int(input("Input %VAT : "))
    result = totalPrice + (vat / 100 * totalPrice)
    return result
def priceCalculate():
    productPrice1 = int(input("Input the product 1st price : "))
    productPrice2 = int(input("Input the product 2nd price : "))
    return vatCalculate(productPrice1+productPrice2)

def allProcessFlow():
    if login() == True :
        showMenu()
        userSelected = selectMenu()
        if userSelected == 1 :
            print(vatCalculate(int(input("Input the price : "))))
        elif userSelected == 2 :
            print(priceCalculate())
    else :
        print("Your username/password are incorrect, please try again")

allProcessFlow()
























