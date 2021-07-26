menuList = []
priceList = []
while True :
    menuName = input("Please enter menu :").capitalize()
    if menuName == "Exit" :
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)
print(menuList,priceList)

def showBill():
    text = "MyFood"
    print(text.center(24,"-"))
    result = 0
    for i in range(len(menuList)):
        result = result + priceList[i]
        print(menuList[i],priceList[i],"THB")
    print("Total :",result,"THB")

showBill()




















































