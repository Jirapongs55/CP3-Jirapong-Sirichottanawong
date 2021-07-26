menuList = []
while True :
    menuName = input("Please enter menu :").capitalize()
    if menuName == "Exit" :
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append([menuName,menuPrice])
print(menuList)

def showBill():
    text = "MyFood"
    print(text.center(24,"-"))
    result = 0
    for i in range(len(menuList)):
        result = result + menuList[i][1]
        print(menuList[i][0],menuList[i][1],"THB")
    print("Total :",result,"THB")

print(menuList)
showBill()





















































