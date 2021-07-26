systemMenu = {"ข้าวหมกไก่":50,"ข้าวมันไก่":40,"ข้าวซอยไก่":60}
menuList = []
while True :
    menuName = input("Please enter menu :").capitalize()
    if menuName == "Exit" :
        break
    else:
       menuList.append([menuName,systemMenu[menuName]])

def showBill():
    text = "MyFood"
    print(text.center(24,"-"))
    result = 0
    for i in range(len(menuList)):
        result = result + menuList[i][1]
        print(menuList[i][0],menuList[i][1])
    print("Total :",result)

print(menuList)
showBill()





















































